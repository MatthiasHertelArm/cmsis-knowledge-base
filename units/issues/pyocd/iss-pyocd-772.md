---
id: "iss-pyocd-772"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32WB55 Nucleo: 'STLink error (9): Get IDCODE error'"
summary: "The maintainer said a failure to read IDCODE usually means the target is not powered or is in a deep sleep mode; this was not confirmed for this board."
status: "draft"
tool: "pyocd"
symptoms: ["0002270:CRITICAL:__main__:STLink error (9): Get IDCODE error"]
symptom_regex: "\\S+:CRITICAL:__main__:STLink\\s+error\\s+\\(\\S+\\):\\s+Get\\s+IDCODE\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/772"
doc_source: "https://github.com/pyocd/pyOCD/issues/772"
resolution: "unresolved"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0002270:CRITICAL:__main__:STLink error (9): Get IDCODE error`

## Cause

The maintainer said a failure to read IDCODE usually means the target is not powered or is in a deep sleep mode; this was not confirmed for this board.

## Fix

Suggested, not confirmed: use a debug build that does not put the device to sleep, or connect with -Oconnect_mode=under-reset (or set connect_mode in a config file). Use the combined pyocd tool rather than the deprecated pyocd-gdbserver.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #772](https://github.com/pyocd/pyOCD/issues/772), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
