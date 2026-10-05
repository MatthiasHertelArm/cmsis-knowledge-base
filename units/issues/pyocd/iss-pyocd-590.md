---
id: "iss-pyocd-590"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd flash with a nonexistent file raises UnboundLocalError instead of a clear message"
summary: "The file-opening error path was broken and the exception class used for reporting was not yet defined."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: local variable 'file_obj' referenced before assignment"]
symptom_regex: "uncaught\\s+exception:\\s+local\\s+variable\\s+'.*?'\\s+referenced\\s+before\\s+assignment"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/590"
doc_source: "https://github.com/pyocd/pyOCD/issues/590"
resolution: "fixed-in-release"
versions: "around 0.19"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: local variable 'file_obj' referenced before assignment`

## Cause

The file-opening error path was broken and the exception class used for reporting was not yet defined.

## Fix

Check the path to the image; use a pyOCD version containing the fix that reports a proper error.

## Source

Resolution: fixed-in-release

Versions: around 0.19

From [pyocd/pyOCD #590](https://github.com/pyocd/pyOCD/issues/590), summarized in own words; confidence medium, not reviewed yet.
