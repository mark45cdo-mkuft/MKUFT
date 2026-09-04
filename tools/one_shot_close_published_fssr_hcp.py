from pathlib import Path
import hashlib
import json
import urllib.request

DOI = "10.5281/zenodo.22309144"
RECORD_ID = "22309144"
TITLE = "Future-Splitting State Recruitment in History-Dependent HCP Magnesium Mechanics: A Minimum-Decisive Prospective Protocol for State Sufficiency, Probe Selection, and Mechanism Localisation"
FILENAME = "FSSR_HCP_MAGNESIUM_MINIMUM_DECISIVE_PROTOCOL_v1.0_DOI_10.5281_zenodo.22309144_FINAL.pdf"
EXPECTED_BYTES = 354874
EXPECTED_MD5 = "00909f843060ee7c108025b0b1148735"
EXPECTED_SHA256 = "52192346256eb3c5895ed466f913b23ce1bb3a8476fdc555edc2abff2dc6646a"
API = f"https://zenodo.org/api/records/{RECORD_ID}"
NL = "\n"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MKUFT-publication-custody-audit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MKUFT-publication-custody-audit/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def must_replace(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected one occurrence, found {n}: {old!r}")
    return text.replace(old, new, 1)


record = fetch_json(API)
doi = record.get("doi") or (((record.get("pids") or {}).get("doi") or {}).get("identifier"))
if doi != DOI:
    raise SystemExit(f"Zenodo DOI mismatch: {doi!r}")

title = (record.get("metadata") or {}).get("title") or record.get("title")
if title != TITLE:
    raise SystemExit(f"Zenodo title mismatch: {title!r}")

doi_status = (((record.get("pids") or {}).get("doi") or {}).get("status"))
if doi_status and doi_status.lower() != "registered":
    raise SystemExit(f"DOI is not registered/published: {doi_status!r}")

conceptdoi = record.get("conceptdoi")
if not conceptdoi:
    conceptdoi = (((record.get("parent") or {}).get("pids") or {}).get("doi") or {}).get("identifier")
if conceptdoi == DOI:
    conceptdoi = None

files_obj = record.get("files") or []
if isinstance(files_obj, list):
    files = files_obj
elif isinstance(files_obj, dict) and isinstance(files_obj.get("entries"), dict):
    files = list(files_obj["entries"].values())
else:
    files = []

matches = []
for item in files:
    size = int(item.get("size") or 0)
    checksum = str(item.get("checksum") or "").lower()
    if size == EXPECTED_BYTES and EXPECTED_MD5 in checksum:
        matches.append(item)
if len(matches) != 1:
    raise SystemExit(f"Expected one exact Zenodo PDF candidate; found {len(matches)}")

zf = matches[0]
links = zf.get("links") or {}
download_url = links.get("content") or links.get("self")
if not download_url:
    raise SystemExit("Zenodo file has no content/self download link")
payload = fetch_bytes(download_url)
if len(payload) != EXPECTED_BYTES:
    raise SystemExit(f"Zenodo byte count mismatch: {len(payload)}")
if hashlib.md5(payload).hexdigest() != EXPECTED_MD5:
    raise SystemExit("Zenodo MD5 mismatch")
if hashlib.sha256(payload).hexdigest() != EXPECTED_SHA256:
    raise SystemExit("Zenodo SHA-256 mismatch")
if not payload.startswith(b"%PDF-"):
    raise SystemExit("Zenodo carrier is not a PDF")

pubdir = Path("publications/FSSR_HCP_MAGNESIUM_MINIMUM_DECISIVE_PROTOCOL_v1.0")
pubdir.mkdir(parents=True, exist_ok=True)
(pubdir / FILENAME).write_bytes(payload)

concept_record_line = f"**Concept DOI:** [`{conceptdoi}`](https://doi.org/{conceptdoi})  {NL}" if conceptdoi else ""
concept_plain_line = f"**Concept DOI:** `{conceptdoi}`  {NL}" if conceptdoi else ""

# Standalone publication record.
p = "FSSR_HCP_MAGNESIUM_PROTOCOL_STANDALONE_PUBLICATION.md"
s = read(p)
s = must_replace(
    s,
    "**Reserved version DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)  " + NL,
    "**Version DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)  " + NL + concept_record_line,
    p,
)
s = must_replace(
    s,
    "**DOI state:** reserved in Zenodo draft; registration and post-publication landing-page verification remain OPEN  " + NL,
    "**DOI state:** PUBLISHED; public Zenodo record and receiver-side PDF verified against the frozen v1.0 identity  " + NL,
    p,
)
old = "The Zenodo draft displayed 354.87 KB and MD5 `00909f843060ee7c108025b0b1148735`, matching the exact locally verified candidate. This closes prepublication carrier selection. It does not yet establish DOI registration or post-publication receiver identity; those gates remain open until publication."
new = f"The published Zenodo record was retrieved through its public record endpoint and the receiver-side PDF was independently matched to the frozen candidate: {EXPECTED_BYTES:,} bytes, MD5 `{EXPECTED_MD5}`, SHA-256 `{EXPECTED_SHA256}`. The exact public carrier is mirrored in the repository publication folder under the same frozen filename."
s = must_replace(s, old, new, p)
s = must_replace(s, "**Zenodo publication/DOI registration:** OPEN until publication is observed.  ", "**Zenodo publication/DOI registration:** CLOSED — DOI registered and public.  ", p)
s = must_replace(s, "**Post-publication receiver-side carrier verification:** OPEN until the published file is read back or otherwise independently matched.", "**Post-publication receiver-side carrier verification:** CLOSED — public Zenodo PDF matched exact byte count, MD5 and SHA-256.", p)
write(p, s)

# Frozen carrier directory.
concept_md = concept_record_line.rstrip("\n")
pub_readme = f"""# FSSR-HCP Magnesium Minimum-Decisive Protocol v1.0 — Frozen DOI Carrier Identity

**Title:** *{TITLE}*  
**Author:** Mark Charles McLaughlin  
**ORCID:** `0009-0005-7736-1511`  
**Version:** 1.0  
**Date:** 4 September 2026  
**Version DOI:** [`{DOI}`](https://doi.org/{DOI})  
{concept_md}
**Status:** PUBLISHED. The public Zenodo receiver-side PDF has been independently retrieved and matched to the frozen v1.0 identity.

## Exact carrier

- Filename: `{FILENAME}`
- Pages: 11
- Bytes: {EXPECTED_BYTES:,}
- MD5: `{EXPECTED_MD5}`
- SHA-256: `{EXPECTED_SHA256}`

The exact public Zenodo carrier is mirrored in this directory. Receiver-side verification matched byte count, MD5 and SHA-256 before the repository mirror was accepted as the frozen DOI carrier.

## Custody boundary

The PDF mirror is the exact verified publication carrier for v1.0. The live Module 28C and GitHub paper route remain later-capable source/canon objects and do not silently rewrite this frozen byte object. The empirical magnesium result remains OPEN; publication and byte identity do not promote the scientific result.

## QA routes

- [Prepublication QA](PREPUBLICATION_QA.md)
- [Postpublication receiver verification](POSTPUBLICATION_QA.md)
- [SHA-256 manifest](SHA256SUMS.txt)
"""
write(pubdir / "README.md", pub_readme)

concept_bullet = f"- Concept DOI: `{conceptdoi}`{NL}" if conceptdoi else ""
postqa = f"""# FSSR-HCP v1.0 — Postpublication Receiver Verification

Date: 4 September 2026

The Zenodo record for version DOI `{DOI}` was retrieved from the public records endpoint after publication. The public receiver-side PDF was then downloaded from the record itself and matched to the frozen prepublication candidate.

- Filename mirrored in repository: `{FILENAME}`
- Pages: 11
- Bytes: {EXPECTED_BYTES:,}
- MD5: `{EXPECTED_MD5}`
- SHA-256: `{EXPECTED_SHA256}`
{concept_bullet}
Result: **PASS — publication/DOI registration and receiver-side byte identity are closed for v1.0.**

This verifies publication-object identity only. It does not establish a positive magnesium result, mechanism discovery, or empirical confirmation of FSSR/FSAI. Those burdens remain owned by the prospective experiment.
"""
write(pubdir / "POSTPUBLICATION_QA.md", postqa)

# Live 28C owner.
p = "docs/28C_FSAI_FSSR_MINIMUM_DECISIVE_FLAGSHIP_HCP_MAGNESIUM_PROTOCOL.md"
s = read(p)
s = must_replace(
    s,
    "**Reserved Zenodo DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144) — reserved for the exact v1.0 carrier; registration remains external until Zenodo publication  ",
    "**Published Zenodo DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144) — v1.0 public record; receiver-side PDF matched to the frozen carrier identity  ",
    p,
)
old = "**Status:** live canonical flagship protocol; design-closed and frozen into a v1.0 publication candidate under reserved DOI `10.5281/zenodo.22309144`. Empirical status remains OPEN: no experiment reported here has been executed by MKUFT, and neither the live module nor the publication carrier reports a positive empirical result, new force, field, constitutive law, twinning mechanism, or completed unification."
new = "**Status:** live canonical flagship protocol; design-closed and published as v1.0 under DOI `10.5281/zenodo.22309144`, with receiver-side publication identity verified. Empirical status remains OPEN: no experiment reported here has been executed by MKUFT, and neither the live module nor the publication carrier reports a positive empirical result, new force, field, constitutive law, twinning mechanism, or completed unification."
s = must_replace(s, old, new, p)
write(p, s)

# Parent owners and front doors.
replacements = {
    "docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md": [("reserved DOI [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)", "published DOI [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)")],
    "docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md": [("reserved DOI [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)", "published DOI [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)")],
    "README.md": [("reserved DOI `10.5281/zenodo.22309144`", "published DOI `10.5281/zenodo.22309144`")],
    "CANON_MAP.md": [("reserved DOI `10.5281/zenodo.22309144`; empirical status remains open", "published DOI `10.5281/zenodo.22309144`; receiver-side carrier verified; empirical status remains open")],
    "FSSR_STANDALONE_PUBLICATION.md": [("reserved DOI `10.5281/zenodo.22309144`; not a new version of FSSR v1.0", "published DOI `10.5281/zenodo.22309144`; not a new version of FSSR v1.0")],
}
for p, reps in replacements.items():
    s = read(p)
    for old, new in reps:
        s = must_replace(s, old, new, p)
    write(p, s)

# Papers index: promote from reserved to Published DOI papers.
p = "papers/README.md"
s = read(p)
h1 = "## DOI-reserved / publication-ready papers" + NL
h2 = "## Published DOI papers" + NL
if s.count(h1) != 1 or s.count(h2) != 1:
    raise SystemExit("papers/README publication section anchors changed")
a = s.index(h1)
b = s.index(h2, a)
block = s[a + len(h1):b].strip()
if block.count("### ") != 1 or "Future-Splitting State Recruitment in History-Dependent HCP Magnesium Mechanics" not in block:
    raise SystemExit("reserved section contains unexpected additional papers; refusing automatic promotion")
block = block.replace("**Reserved version DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)  ", "**Version DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)  ")
if conceptdoi and "**Concept DOI:**" not in block:
    marker = "**Version DOI:** [`10.5281/zenodo.22309144`](https://doi.org/10.5281/zenodo.22309144)  " + NL
    block = block.replace(marker, marker + f"**Concept DOI:** [`{conceptdoi}`](https://doi.org/{conceptdoi})  " + NL, 1)
block = block.replace("**Status:** exact v1.0 carrier frozen and visually audited; Zenodo DOI registration/published-state verification remains external until the draft is published  ", "**Status:** published v1.0 Zenodo preprint; receiver-side PDF matched to the frozen carrier identity  ")
block = block.replace("- [Frozen carrier identity/checksum record](../publications/FSSR_HCP_MAGNESIUM_MINIMUM_DECISIVE_PROTOCOL_v1.0/)", "- [Frozen DOI PDF mirror and identity/checksum record](../publications/FSSR_HCP_MAGNESIUM_MINIMUM_DECISIVE_PROTOCOL_v1.0/)" + NL + "- [Zenodo v1.0 publication](https://doi.org/10.5281/zenodo.22309144)")
after = s[b + len(h2):]
s = s[:a] + h2 + NL + block + NL + NL + after.lstrip("\n")
write(p, s)

# Provenance section only.
p = "PROVENANCE_DOI_AND_ATTRIBUTION.md"
s = read(p)
start = "## FSSR-HCP minimum-decisive flagship protocol" + NL
end = "## Bell Constraints as Typed Boundaries" + NL
if s.count(start) != 1 or s.count(end) != 1:
    raise SystemExit("provenance FSSR-HCP section anchors changed")
a = s.index(start)
b = s.index(end, a)
sec = s[a:b]
sec = must_replace(sec, "**Reserved version DOI:** `10.5281/zenodo.22309144`  ", "**Version DOI:** `10.5281/zenodo.22309144`  ", "provenance section")
if conceptdoi and "**Concept DOI:**" not in sec:
    marker = "**Version DOI:** `10.5281/zenodo.22309144`  " + NL
    sec = sec.replace(marker, marker + concept_plain_line, 1)
sec = must_replace(sec, "**DOI state at repository fold:** reserved in a Zenodo draft; registration/published-state verification remains OPEN until publication is observed  ", "**DOI state:** PUBLISHED; receiver-side public PDF verified against the frozen v1.0 byte identity  ", "provenance section")
sec = sec.replace("Public/custody routes:" + NL + NL, "Public/custody routes:" + NL + NL + "- [Zenodo v1.0 publication](https://doi.org/10.5281/zenodo.22309144)" + NL, 1)
s = s[:a] + sec + s[b:]
write(p, s)

# Publication SOP: close full custody transition.
p = "RENDERING_AND_PUBLICATION_INTEGRITY.md"
s = read(p)
old = f"For the FSSR-HCP v1.0 candidate, the exact intended carrier is 11 pages, 354,874 bytes, MD5 `{EXPECTED_MD5}`, SHA-256 `{EXPECTED_SHA256}`. The Zenodo draft displayed the same file size and MD5 before publication. That is strong prepublication receiver-side candidate identity; DOI registration and final post-publication receiver verification remain separate gates."
new = f"For FSSR-HCP v1.0, the exact carrier is 11 pages, 354,874 bytes, MD5 `{EXPECTED_MD5}`, SHA-256 `{EXPECTED_SHA256}`. Prepublication Zenodo draft metadata matched size and MD5; after publication, the public Zenodo carrier was downloaded from the record and independently matched in byte count, MD5 and SHA-256 before the repository accepted it as the frozen DOI mirror. This closes the full candidate → published receiver → verified mirror custody chain without changing the empirical status of the magnesium experiment."
s = must_replace(s, old, new, p)
write(p, s)

# Stale-state guard.
targets = [
    "FSSR_HCP_MAGNESIUM_PROTOCOL_STANDALONE_PUBLICATION.md",
    "docs/28C_FSAI_FSSR_MINIMUM_DECISIVE_FLAGSHIP_HCP_MAGNESIUM_PROTOCOL.md",
    "docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md",
    "docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md",
    "README.md",
    "CANON_MAP.md",
    "FSSR_STANDALONE_PUBLICATION.md",
    "papers/README.md",
    "PROVENANCE_DOI_AND_ATTRIBUTION.md",
    "RENDERING_AND_PUBLICATION_INTEGRITY.md",
    str(pubdir / "README.md"),
    str(pubdir / "POSTPUBLICATION_QA.md"),
]
stale = [
    "reserved DOI `10.5281/zenodo.22309144`",
    "Reserved version DOI",
    "Zenodo publication/DOI registration:** OPEN",
    "Post-publication receiver-side carrier verification:** OPEN",
]
for target in targets:
    txt = read(target)
    for token in stale:
        if token in txt:
            raise SystemExit(f"stale publication state remains in {target}: {token}")

print(json.dumps({"doi": DOI, "conceptdoi": conceptdoi, "bytes": len(payload), "md5": EXPECTED_MD5, "sha256": EXPECTED_SHA256}, indent=2))
