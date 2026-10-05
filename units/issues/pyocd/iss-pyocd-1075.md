---
id: "iss-pyocd-1075"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Running tools/pyocd.py from a build tree: 'relative import beyond top-level package'"
summary: "The scripts under pyocd/tools are deprecated modules and not entry points; running them directly from a build tree breaks their relative imports."
status: "draft"
tool: "pyocd"
symptoms: ["ValueError: attempted relative import beyond top-level package"]
symptom_regex: "ValueError:\\s+attempted\\s+relative\\s+import\\s+beyond\\s+top\\-level\\s+package"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1075"
doc_source: "https://github.com/pyocd/pyOCD/issues/1075"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ValueError: attempted relative import beyond top-level package`

## Cause

The scripts under pyocd/tools are deprecated modules and not entry points; running them directly from a build tree breaks their relative imports.

## Fix

Run the installed `pyocd` executable or `python -m pyocd`. For development, install into a virtualenv with `pip install -e .` instead of `setup.py install`.

## Source

Resolution: user-error

From [pyocd/pyOCD #1075](https://github.com/pyocd/pyOCD/issues/1075), summarized in own words; confidence high, checked against the thread, not reviewed yet.
