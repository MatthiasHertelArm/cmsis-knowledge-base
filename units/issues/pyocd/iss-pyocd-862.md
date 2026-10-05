---
id: "iss-pyocd-862"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: MIMXRT1050-EVK stops connecting after flashing: 'No cores were discovered'"
summary: "The application goes to deep sleep soon after reset (for example Mbed wait(0.2) with no other thread), and on this target the debugger cannot reconnect to a sleeping core; connect under reset did not help."
status: "draft"
tool: "pyocd"
symptoms: ["No cores were discovered!"]
symptom_regex: "No\\s+cores\\s+were\\s+discovered!"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/862"
doc_source: "https://github.com/pyocd/pyOCD/issues/862"
resolution: "workaround"
versions: "0.26.0"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT1050"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No cores were discovered!`

## Cause

The application goes to deep sleep soon after reset (for example Mbed wait(0.2) with no other thread), and on this target the debugger cannot reconnect to a sleeping core; connect under reset did not help.

## Fix

Keep the target awake in debug builds: use wait_us() instead of wait(), or define the MBED_DEBUG macro to disable deep sleep. Recover a locked-out board with the DIP switch and erase.

## Source

Resolution: workaround

Versions: 0.26.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #862](https://github.com/pyocd/pyOCD/issues/862), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
