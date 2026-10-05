---
id: "iss-pyocd-1004"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Building a standalone pyocd executable with PyInstaller fails"
summary: "Pointing PyInstaller at pyocd/tools/pyocd.py breaks its relative imports; later problems came from prettytable's pkg_resources distribution lookup and the SVD data zip not being bundled."
status: "draft"
tool: "pyocd"
symptoms: ["ImportError: attempted relative import with no known parent package"]
symptom_regex: "ImportError:\\s+attempted\\s+relative\\s+import\\s+with\\s+no\\s+known\\s+parent\\s+package"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1004"
doc_source: "https://github.com/pyocd/pyOCD/issues/1004"
resolution: "fixed-in-release"
versions: "0.28.1.dev54 (reporter's source build)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ImportError: attempted relative import with no known parent package`

## Cause

Pointing PyInstaller at pyocd/tools/pyocd.py breaks its relative imports; later problems came from prettytable's pkg_resources distribution lookup and the SVD data zip not being bundled.

## Fix

Use the prebuilt binary distributions included in the pyOCD release assets instead of building your own.

## Source

Resolution: fixed-in-release

Versions: 0.28.1.dev54 (reporter's source build)

From [pyocd/pyOCD #1004](https://github.com/pyocd/pyOCD/issues/1004), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
