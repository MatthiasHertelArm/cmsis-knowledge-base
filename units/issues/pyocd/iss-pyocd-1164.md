---
id: "iss-pyocd-1164"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd warns that module 'hid' has no attribute 'device'"
summary: "The wrong Python package providing the 'hid' module was installed by hand (pyhidapi instead of the Cython hidapi binding that pyOCD expects)."
status: "draft"
tool: "pyocd"
symptoms: ["module 'hid' has no attribute 'device'"]
symptom_regex: "module\\s+'.*?'\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1164"
doc_source: "https://github.com/pyocd/pyOCD/issues/1164"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`module 'hid' has no attribute 'device'`

## Cause

The wrong Python package providing the 'hid' module was installed by hand (pyhidapi instead of the Cython hidapi binding that pyOCD expects).

## Fix

Remove the wrong package and let pip install pyOCD's own dependencies; the correct one is the PyPI package named 'hidapi' (cython-hidapi).

## Source

Resolution: user-error

From [pyocd/pyOCD #1164](https://github.com/pyocd/pyOCD/issues/1164), summarized in own words; confidence high, not reviewed yet.
