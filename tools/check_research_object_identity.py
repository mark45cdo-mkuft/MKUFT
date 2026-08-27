#!/usr/bin/env python3
"""Deterministic research-object identity and release-manifest checks for MKUFT."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$", re.I)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$", re.I)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ORCID_RE = re.compile(r"\b\d{4}-\d{4}-\d{4}-\d{3}[\dX]\b")
DOI_IN_TEXT_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"']+")

MODULE_PATH = Path("docs/34_RESEARCH_OBJECT_IDENTITY_RELEASE_INTEGRITY_AND_REPRODUCIBILITY.md")
MANIFEST_DIR = Path("release-manifests")
TEMPLATE_NAME = "_template.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _first_orcid(text: str) -> str | None:
    match = ORCID_RE.search(text)
    return match.group(0) if match else None


def _preferred_doi_from_cff(text: str) -> str | None:
    marker = "preferred-citation:"
    tail = text.split(marker, 1)[1] if marker in text else text
    match = re.search(r"(?m)^\s*doi:\s*[\"']?([^\s\"']+)", tail)
    return match.group(1) if match else None


def _repo_url_from_cff(text: str) -> str | None:
    match = re.search(r"(?m)^repository-code:\s*[\"']?([^\s\"']+)", text)
    return match.group(1) if match else None


def _normalised_orcid(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    return _first_orcid(value)


def check_manifest(root: Path, manifest_path: Path) -> list[str]:
    errors: list[str] = []
    rel = manifest_path.relative_to(root)
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{rel}: invalid JSON ({exc})"]

    if data.get("schema_version") != "1.0":
        errors.append(f"{rel}: schema_version must be '1.0'")
    if not isinstance(data.get("release_id"), str) or not data["release_id"].strip():
        errors.append(f"{rel}: release_id must be a non-empty string")
    if not isinstance(data.get("tag"), str) or not data["tag"].strip():
        errors.append(f"{rel}: tag must be a non-empty string")

    commit = data.get("commit")
    if not isinstance(commit, str) or not SHA40_RE.fullmatch(commit):
        errors.append(f"{rel}: commit must be a 40-character hexadecimal Git SHA")

    citation = data.get("citation")
    if not isinstance(citation, dict):
        errors.append(f"{rel}: citation must be an object")
    else:
        if not isinstance(citation.get("version"), str) or not citation["version"].strip():
            errors.append(f"{rel}: citation.version must be a non-empty string")
        date = citation.get("date")
        if not isinstance(date, str) or not DATE_RE.fullmatch(date):
            errors.append(f"{rel}: citation.date must use YYYY-MM-DD")
        doi = citation.get("doi")
        if doi not in (None, "") and (not isinstance(doi, str) or not DOI_RE.fullmatch(doi)):
            errors.append(f"{rel}: citation.doi must be blank or a DOI")

    identifiers = data.get("external_identifiers", [])
    if not isinstance(identifiers, list):
        errors.append(f"{rel}: external_identifiers must be a list when present")
    else:
        for idx, item in enumerate(identifiers):
            if not isinstance(item, dict) or not isinstance(item.get("type"), str) or not isinstance(item.get("value"), str):
                errors.append(f"{rel}: external_identifiers[{idx}] must contain string type and value")

    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append(f"{rel}: artifacts must be a non-empty list")
        return errors

    seen_paths: set[str] = set()
    for idx, artifact in enumerate(artifacts):
        prefix = f"{rel}: artifacts[{idx}]"
        if not isinstance(artifact, dict):
            errors.append(f"{prefix} must be an object")
            continue

        path_value = artifact.get("path")
        if not isinstance(path_value, str) or not path_value.strip():
            errors.append(f"{prefix}.path must be a non-empty repository-relative path")
            continue

        candidate = Path(path_value)
        if candidate.is_absolute() or ".." in candidate.parts or path_value.startswith("./"):
            errors.append(f"{prefix}.path must be a normalised repository-relative path")
            continue
        if path_value in seen_paths:
            errors.append(f"{prefix}.path duplicates another artifact path")
            continue
        seen_paths.add(path_value)

        digest = artifact.get("sha256")
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            errors.append(f"{prefix}.sha256 must be 64 hexadecimal characters")

        byte_count = artifact.get("bytes")
        if not isinstance(byte_count, int) or isinstance(byte_count, bool) or byte_count < 0:
            errors.append(f"{prefix}.bytes must be a non-negative integer")

        file_path = root / candidate
        if not file_path.is_file():
            errors.append(f"{prefix}.path does not exist: {path_value}")
            continue

        if isinstance(byte_count, int) and not isinstance(byte_count, bool) and file_path.stat().st_size != byte_count:
            errors.append(f"{prefix}.bytes mismatch: manifest={byte_count} actual={file_path.stat().st_size}")
        if isinstance(digest, str) and SHA256_RE.fullmatch(digest):
            actual = sha256_file(file_path)
            if actual.lower() != digest.lower():
                errors.append(f"{prefix}.sha256 mismatch: manifest={digest} actual={actual}")

    return errors


def check_root(root: Path) -> list[str]:
    errors: list[str] = []

    required = [
        root / "CITATION.cff",
        root / "codemeta.json",
        root / MODULE_PATH,
        root / MANIFEST_DIR / "README.md",
        root / MANIFEST_DIR / TEMPLATE_NAME,
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"missing required research-object identity carrier: {path.relative_to(root)}")

    if errors:
        return errors

    cff_text = (root / "CITATION.cff").read_text(encoding="utf-8")
    try:
        codemeta = json.loads((root / "codemeta.json").read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"codemeta.json is not valid JSON: {exc}")
        codemeta = {}

    if "cff-version: 1.2.0" not in cff_text:
        errors.append("CITATION.cff must retain CFF 1.2.0 identity")

    cff_orcid = _first_orcid(cff_text)
    cm_author = codemeta.get("author") if isinstance(codemeta, dict) else None
    cm_orcid = _normalised_orcid(cm_author.get("identifier")) if isinstance(cm_author, dict) else None
    if not cff_orcid or not cm_orcid or cff_orcid != cm_orcid:
        errors.append(f"ORCID mismatch between CITATION.cff ({cff_orcid}) and codemeta.json ({cm_orcid})")

    cff_doi = _preferred_doi_from_cff(cff_text)
    cm_identifier = codemeta.get("identifier") if isinstance(codemeta, dict) else None
    cm_doi = None
    if isinstance(cm_identifier, str):
        match = DOI_IN_TEXT_RE.search(cm_identifier)
        cm_doi = match.group(0) if match else None
    if not cff_doi or not cm_doi or cff_doi != cm_doi:
        errors.append(f"principal DOI mismatch between CITATION.cff ({cff_doi}) and codemeta.json ({cm_doi})")

    cff_repo = _repo_url_from_cff(cff_text)
    cm_url = codemeta.get("url") if isinstance(codemeta, dict) else None
    if not cff_repo or not isinstance(cm_url, str) or cff_repo.rstrip("/") != cm_url.rstrip("/"):
        errors.append(f"repository URL mismatch between CITATION.cff ({cff_repo}) and codemeta.json ({cm_url})")

    if (root / ".zenodo.json").exists():
        errors.append(
            ".zenodo.json is present while CITATION.cff is the declared repository citation metadata carrier; "
            "a metadata-authority transition requires an explicit Module 34/checker revision in the same change"
        )

    manifest_dir = root / MANIFEST_DIR
    for path in sorted(manifest_dir.glob("*.json")):
        if path.name == TEMPLATE_NAME:
            continue
        errors.extend(check_manifest(root, path))

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check_root(root)
    if errors:
        print("Research-object identity check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Research-object identity check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
