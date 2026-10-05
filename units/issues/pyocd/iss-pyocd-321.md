---
id: "iss-pyocd-321"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver appears to hang or fails with SyntaxError on Windows"
summary: "Old pyOCD only runs on Python 2; under Python 3 the entry point raises SyntaxError."
status: "draft"
tool: "pyocd"
symptoms: ["SyntaxError: invalid syntax"]
symptom_regex: "SyntaxError:\\s+invalid\\s+syntax"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/321"
doc_source: "https://github.com/pyocd/pyOCD/issues/321"
resolution: "user-error"
versions: "0.8.1a1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`SyntaxError: invalid syntax`

## Cause

Old pyOCD only runs on Python 2; under Python 3 the entry point raises SyntaxError. Without a recognised board the server simply waits for one, and K64F firmware older than 0242 needs the Windows serial driver to be visible.

## Fix

Use Python 2.7 with that pyOCD version, update the interface firmware (0242 or newer) or install the mbed serial driver, and confirm the board is listed with `-l`.

## Source

Resolution: user-error

Versions: 0.8.1a1

From [pyocd/pyOCD #321](https://github.com/pyocd/pyOCD/issues/321), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
