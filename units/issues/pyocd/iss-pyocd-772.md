---
id: "iss-pyocd-772"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32WB55 Nucleo: 'STLink error (9): Get IDCODE error'"
summary: "Failure to read IDCODE usually means the target is unpowered or in deep sleep."
status: "draft"
tool: "pyocd"
symptoms: ["0002270:CRITICAL:__main__:STLink error (9): Get IDCODE error"]
symptom_regex: "\\S+:CRITICAL:__main__:STLink\\s+error\\s+\\(\\S+\\):\\s+Get\\s+IDCODE\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/772"
doc_source: "https://github.com/pyocd/pyOCD/issues/772"
resolution: "configuration"
versions: "0.2x"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0002270:CRITICAL:__main__:STLink error (9): Get IDCODE error`

## Cause

Failure to read IDCODE usually means the target is unpowered or in deep sleep.

## Fix

Use a debug build that does not sleep, or connect with -Oconnect_mode=under-reset (or set it in pyocd.yaml). Prefer the combined 'pyocd' tool over pyocd-gdbserver.

## Source

Resolution: configuration

Versions: 0.2x

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #772](https://github.com/pyocd/pyOCD/issues/772), summarized in own words; confidence medium, not reviewed yet.
