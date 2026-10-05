---
id: "iss-pyocd-802"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing via gdb fails: type object 'Target' has no attribute 'CATCH_CORE_RESET'"
summary: "Regression after CATCH_CORE_RESET was renamed: the LPC1768 built-in target's set_reset_catch still used the old name, so reset-and-halt during flashing raised AttributeError."
status: "draft"
tool: "pyocd"
symptoms: ["Unhandled exception in handle_message: type object 'Target' has no attribute 'CATCH_CORE_RESET'"]
symptom_regex: "Unhandled\\s+exception\\s+in\\s+handle_message:\\s+type\\s+object\\s+'.*?'\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/802"
doc_source: "https://github.com/pyocd/pyOCD/issues/802"
resolution: "fixed-in-release"
versions: "0.24.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC1768"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unhandled exception in handle_message: type object 'Target' has no attribute 'CATCH_CORE_RESET'`

## Cause

Regression after CATCH_CORE_RESET was renamed: the LPC1768 built-in target's set_reset_catch still used the old name, so reset-and-halt during flashing raised AttributeError.

## Fix

Fixed by PR #821, merged to master; use a pyOCD version that includes it.

## Source

Resolution: fixed-in-release

Versions: 0.24.1

From [pyocd/pyOCD #802](https://github.com/pyocd/pyOCD/issues/802), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
