---
id: "iss-pyocd-1004"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Building a standalone pyocd executable with PyInstaller fails"
summary: "Pointing PyInstaller at pyocd/tools/pyocd.py breaks relative imports; later problems came from prettytable's pkg_resources distribution lookup and the SVD data zip not being bundled."
status: "draft"
tool: "pyocd"
symptoms: ["ImportError: attempted relative import with no known parent package"]
symptom_regex: "ImportError:\\s+attempted\\s+relative\\s+import\\s+with\\s+no\\s+known\\s+parent\\s+package"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1004"
doc_source: "https://github.com/pyocd/pyOCD/issues/1004"
resolution: "fixed-in-release"
versions: "binaries shipped in releases after the 0.2x line"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ImportError: attempted relative import with no known parent package`

## Cause

Pointing PyInstaller at pyocd/tools/pyocd.py breaks relative imports; later problems came from prettytable's pkg_resources distribution lookup and the SVD data zip not being bundled.

## Fix

Use the prebuilt binary distributions that are attached to the pyOCD release assets instead of building your own.

## Source

Resolution: fixed-in-release

Versions: binaries shipped in releases after the 0.2x line

From [pyocd/pyOCD #1004](https://github.com/pyocd/pyOCD/issues/1004), summarized in own words; confidence medium, not reviewed yet.
