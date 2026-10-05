---
id: "iss-pyocd-986"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Semihosting output over gdbserver raises TypeError 'string argument without an encoding'"
summary: "A string/bytes conversion bug in the semihosting request handler (debug/semihost.py) broke every semihost call under Python 3."
status: "draft"
tool: "pyocd"
symptoms: ["Unhandled exception in handle_message: string argument without an encoding"]
symptom_regex: "Unhandled\\s+exception\\s+in\\s+handle_message:\\s+string\\s+argument\\s+without\\s+an\\s+encoding"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/986"
doc_source: "https://github.com/pyocd/pyOCD/issues/986"
resolution: "fixed-in-release"
versions: "seen with 0.28.x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52840"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unhandled exception in handle_message: string argument without an encoding`

## Cause

A string/bytes conversion bug in the semihosting request handler (debug/semihost.py) broke every semihost call under Python 3.

## Fix

Update to a pyOCD release after 0.28.x that contains the maintainer's fix (the semihost unit test that would have caught it had been disabled).

## Source

Resolution: fixed-in-release

Versions: seen with 0.28.x

From [pyocd/pyOCD #986](https://github.com/pyocd/pyOCD/issues/986), summarized in own words; confidence medium, not reviewed yet.
