---
id: "iss-pyocd-755"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Debugging pyocd __main__.py from an IDE: 'Attempted relative import in non-package'"
summary: "The IDE runs pyocd/__main__.py as a plain script, so Python does not treat it as part of the pyocd package."
status: "draft"
tool: "pyocd"
symptoms: ["ValueError: Attempted relative import in non-package"]
symptom_regex: "ValueError:\\s+Attempted\\s+relative\\s+import\\s+in\\s+non\\-package"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/755"
doc_source: "https://github.com/pyocd/pyOCD/issues/755"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ValueError: Attempted relative import in non-package`

## Cause

The IDE runs pyocd/__main__.py as a plain script, so Python does not treat it as part of the pyocd package.

## Fix

Run it as a module (`python -m pyocd`) in a virtualenv with pyocd installed; in the IDE configure a module run target named pyocd instead of a script path.

## Source

Resolution: user-error

From [pyocd/pyOCD #755](https://github.com/pyocd/pyOCD/issues/755), summarized in own words; confidence high, checked against the thread, not reviewed yet.
