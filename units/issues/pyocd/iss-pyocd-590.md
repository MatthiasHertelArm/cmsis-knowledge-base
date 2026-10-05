---
id: "iss-pyocd-590"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd flash with a nonexistent file raises UnboundLocalError instead of a clear message"
summary: "The image file passed to pyocd flash does not exist, and the loader's error path then closes a file object that was never assigned; a proper error also needs the ArgumentError class that PR #587 adds."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: local variable 'file_obj' referenced before assignment"]
symptom_regex: "uncaught\\s+exception:\\s+local\\s+variable\\s+'.*?'\\s+referenced\\s+before\\s+assignment"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/590"
doc_source: "https://github.com/pyocd/pyOCD/issues/590"
resolution: "unresolved"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: local variable 'file_obj' referenced before assignment`

## Cause

The image file passed to pyocd flash does not exist, and the loader's error path then closes a file object that was never assigned; a proper error also needs the ArgumentError class that PR #587 adds.

## Fix

Check that the image path exists. The misleading exception was to be fixed once PR #587 is merged; no release is named.

## Source

Resolution: unresolved

From [pyocd/pyOCD #590](https://github.com/pyocd/pyOCD/issues/590), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
