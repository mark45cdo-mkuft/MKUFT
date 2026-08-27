#!/usr/bin/env python3
"""Fixture tests for the research-object identity checker."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

CHECKER_PATH = Path(__file__).with_name("check_research_object_identity.py")
spec = importlib.util.spec_from_file_location("research_object_checker", CHECKER_PATH)
checker = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(checker)


class ResearchObjectIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "release-manifests").mkdir()
        (self.root / "docs" / "34_RESEARCH_OBJECT_IDENTITY_RELEASE_INTEGRITY_AND_REPRODUCIBILITY.md").write_text(
            "# 34\n", encoding="utf-8"
        )
        (self.root / "release-manifests" / "README.md").write_text("# manifests\n", encoding="utf-8")
        (self.root / "release-manifests" / "_template.json").write_text("{}\n", encoding="utf-8")
        (self.root / "CITATION.cff").write_text(
            """cff-version: 1.2.0
repository-code: "https://github.com/example/repo"
authors:
  - family-names: "Example"
    given-names: "Researcher"
    orcid: "https://orcid.org/0000-0000-0000-000X"
preferred-citation:
  type: generic
  doi: "10.5281/zenodo.12345"
""",
            encoding="utf-8",
        )
        (self.root / "codemeta.json").write_text(
            json.dumps(
                {
                    "identifier": "https://doi.org/10.5281/zenodo.12345",
                    "url": "https://github.com/example/repo",
                    "author": {"identifier": "https://orcid.org/0000-0000-0000-000X"},
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_valid_manifest(self, *, digest: str | None = None, path: str = "artifact.txt") -> None:
        artifact = self.root / "artifact.txt"
        artifact.write_text("research object\n", encoding="utf-8")
        actual_digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
        manifest = {
            "schema_version": "1.0",
            "release_id": "example-v1",
            "tag": "v1.0.0",
            "commit": "a" * 40,
            "citation": {"version": "1.0", "date": "2026-08-27", "doi": "10.5281/zenodo.12345"},
            "artifacts": [
                {
                    "path": path,
                    "sha256": digest or actual_digest,
                    "bytes": artifact.stat().st_size,
                }
            ],
        }
        (self.root / "release-manifests" / "example-v1.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )

    def test_valid_baseline_without_concrete_manifest_passes(self) -> None:
        self.assertEqual(checker.check_root(self.root), [])

    def test_exact_manifest_passes(self) -> None:
        self.write_valid_manifest()
        self.assertEqual(checker.check_root(self.root), [])

    def test_digest_mismatch_fails(self) -> None:
        self.write_valid_manifest(digest="0" * 64)
        errors = checker.check_root(self.root)
        self.assertTrue(any("sha256 mismatch" in error for error in errors))

    def test_path_traversal_fails(self) -> None:
        self.write_valid_manifest(path="../artifact.txt")
        errors = checker.check_root(self.root)
        self.assertTrue(any("normalised repository-relative path" in error for error in errors))

    def test_undeclared_metadata_authority_fails(self) -> None:
        (self.root / ".zenodo.json").write_text("{}\n", encoding="utf-8")
        errors = checker.check_root(self.root)
        self.assertTrue(any("declared repository citation metadata carrier" in error for error in errors))

    def test_principal_doi_mismatch_fails(self) -> None:
        data = json.loads((self.root / "codemeta.json").read_text(encoding="utf-8"))
        data["identifier"] = "https://doi.org/10.5281/zenodo.99999"
        (self.root / "codemeta.json").write_text(json.dumps(data), encoding="utf-8")
        errors = checker.check_root(self.root)
        self.assertTrue(any("principal DOI mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
