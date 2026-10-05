---
id: "iss-pyocd-527"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list crashes on macOS when hidapi returns the product name as bytes"
summary: "On macOS with Python 3, hid.enumerate() can return the product string as bytes, and the CMSIS-DAP name check in hidapi_backend.py searched it with a str."
status: "draft"
tool: "pyocd"
symptoms: ["0000350:ERROR:__main__:uncaught exception: argument should be integer or bytes-like object, not 'str'"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+argument\\s+should\\s+be\\s+integer\\s+or\\s+bytes\\-like\\s+object,\\s+not\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/527"
doc_source: "https://github.com/pyocd/pyOCD/issues/527"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000350:ERROR:__main__:uncaught exception: argument should be integer or bytes-like object, not 'str'`

## Cause

On macOS with Python 3, hid.enumerate() can return the product string as bytes, and the CMSIS-DAP name check in hidapi_backend.py searched it with a str.

## Fix

Convert the product string to str before searching for 'CMSIS-DAP' in hidapi_backend.py, as the reporter did and proposed in PR #526.

## Source

Resolution: workaround

From [pyocd/pyOCD #527](https://github.com/pyocd/pyOCD/issues/527), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
