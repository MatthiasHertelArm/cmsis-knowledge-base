---
id: "iss-pyocd-527"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list crashes on macOS when hidapi returns the product name as bytes"
summary: "On Python 3 with macOS, hid.enumerate can return the product string as bytes, and the CMSIS-DAP name check used a str search on it."
status: "draft"
tool: "pyocd"
symptoms: ["0000350:ERROR:__main__:uncaught exception: argument should be integer or bytes-like object, not 'str'"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+argument\\s+should\\s+be\\s+integer\\s+or\\s+bytes\\-like\\s+object,\\s+not\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/527"
doc_source: "https://github.com/pyocd/pyOCD/issues/527"
resolution: "fixed-in-release"
versions: "around 0.17 to 0.19"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000350:ERROR:__main__:uncaught exception: argument should be integer or bytes-like object, not 'str'`

## Cause

On Python 3 with macOS, hid.enumerate can return the product string as bytes, and the CMSIS-DAP name check used a str search on it.

## Fix

Update to a pyOCD with the fix (PR #526 era) that converts the name to str.

## Source

Resolution: fixed-in-release

Versions: around 0.17 to 0.19

From [pyocd/pyOCD #527](https://github.com/pyocd/pyOCD/issues/527), summarized in own words; confidence medium, not reviewed yet.
