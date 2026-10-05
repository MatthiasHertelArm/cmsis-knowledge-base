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
resolution: "workaround"
versions: "DAPLink 0243, pyOCD 0.8 era"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:Unhandled exception in handleMsg:`

## Cause

On macOS closing a serial port sends a break, and DAPLink treats a serial break as a command to reset the target; pyocd does not expect the target to reset under it and fails reading registers.

## Fix

Avoid closing the serial terminal during a debug session on macOS (or use a terminal that does not send break on close). Newer DAPLink may allow disabling reset-on-break; no pyocd setting existed.

## Source

Resolution: workaround

Versions: DAPLink 0243, pyOCD 0.8 era

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #309](https://github.com/pyocd/pyOCD/issues/309), summarized in own words; confidence medium, not reviewed yet.
