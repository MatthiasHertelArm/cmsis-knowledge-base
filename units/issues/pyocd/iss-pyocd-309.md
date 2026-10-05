---
id: "iss-pyocd-309"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdbserver crashes when a serial terminal on a K64F is closed (macOS)"
summary: "On macOS closing a serial port sends a break, and DAPLink treats a serial break as a command to reset the target; pyocd does not expect the target to reset under it and fails reading registers."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:Unhandled exception in handleMsg:"]
symptom_regex: "Unhandled\\s+exception\\s+in\\s+handleMsg:"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/309"
doc_source: "https://github.com/pyocd/pyOCD/issues/309"
resolution: "unresolved"
versions: "DAPLink interface 0243"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:Unhandled exception in handleMsg:`

## Cause

On macOS closing a serial port sends a break, and DAPLink treats a serial break as a command to reset the target; pyocd does not expect the target to reset under it and fails reading registers.

## Fix

No fix in the thread: a DAPLink option to disable reset-on-break and reset detection in pyOCD were only proposed, and the issue still existed later. The reporter used OpenOCD instead, where the session stops but does not crash.

## Source

Resolution: unresolved

Versions: DAPLink interface 0243

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #309](https://github.com/pyocd/pyOCD/issues/309), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
