---
id: "iss-pyocd-800"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ImportError: cannot import name 'FlashEraser' from 'pyocd.flash.loader' after upgrading"
summary: "pyOCD 0.24.0 refactored its Python API and moved classes out of pyocd.flash.loader; a third-party tool built on the old API breaks."
status: "draft"
tool: "pyocd"
symptoms: ["ImportError: cannot import name 'FlashEraser' from 'pyocd.flash.loader'"]
symptom_regex: "ImportError:\\s+cannot\\s+import\\s+name\\s+'.*?'\\s+from\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/800"
doc_source: "https://github.com/pyocd/pyOCD/issues/800"
resolution: "not-a-bug"
versions: "API change in 0.24.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ImportError: cannot import name 'FlashEraser' from 'pyocd.flash.loader'`

## Cause

pyOCD 0.24.0 refactored its Python API and moved classes out of pyocd.flash.loader; a third-party tool built on the old API breaks.

## Fix

Pin the pyOCD version required by the third-party tool (the Python API is unstable before 1.0) or update that tool.

## Source

Resolution: not-a-bug

Versions: API change in 0.24.0

From [pyocd/pyOCD #800](https://github.com/pyocd/pyOCD/issues/800), summarized in own words; confidence high, not reviewed yet.
