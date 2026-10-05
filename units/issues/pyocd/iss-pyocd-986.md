---
id: "iss-pyocd-986"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Semihosting output over gdbserver raises TypeError 'string argument without an encoding'"
summary: "A string/bytes conversion bug in SemihostAgent._get_string() (six.ensure_str(bytes(bytearray(''))...)) raises TypeError for semihosting write requests under Python 3."
status: "draft"
tool: "pyocd"
symptoms: ["Unhandled exception in handle_message: string argument without an encoding"]
symptom_regex: "Unhandled\\s+exception\\s+in\\s+handle_message:\\s+string\\s+argument\\s+without\\s+an\\s+encoding"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/986"
doc_source: "https://github.com/pyocd/pyOCD/issues/986"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["nRF52840"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unhandled exception in handle_message: string argument without an encoding`

## Cause

A string/bytes conversion bug in SemihostAgent._get_string() (six.ensure_str(bytes(bytearray(''))...)) raises TypeError for semihosting write requests under Python 3.

## Fix

Fixed by the maintainer's commit, which the reporter confirmed works. Before that, replacing the failing line in _get_string() with target_str = "" removed the error.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #986](https://github.com/pyocd/pyOCD/issues/986), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
