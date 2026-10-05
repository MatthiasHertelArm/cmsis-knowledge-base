---
id: "iss-pyocd-1129"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PowerShell window closes after pyocd list, flash or reset on Windows"
summary: "The crash comes from PowerShell's own console key reader (PSReadLine) after pyocd has used the console, not from the probe or target."
status: "draft"
tool: "pyocd"
symptoms: ["Unhandled exception. System.ArgumentOutOfRangeException: Console key values must be between 0 and 255 inclusive. (Parameter 'key')"]
symptom_regex: "Unhandled\\s+exception\\.\\s+System\\.ArgumentOutOfRangeException:\\s+Console\\s+key\\s+values\\s+must\\s+be\\s+between\\s+\\S+\\s+and\\s+\\S+\\s+inclusive\\.\\s+\\(Parameter\\s+'.*?'\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1129"
doc_source: "https://github.com/pyocd/pyOCD/issues/1129"
resolution: "workaround"
versions: "pyOCD 0.29 to 0.32 on Windows 10/11"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unhandled exception. System.ArgumentOutOfRangeException: Console key values must be between 0 and 255 inclusive. (Parameter 'key')`

## Cause

The crash comes from PowerShell's own console key reader (PSReadLine) after pyocd has used the console, not from the probe or target. It reproduces with Windows PowerShell 5.1 and 7.x but not with cmd.exe.

## Fix

Run pyocd from cmd.exe (also works when started from a PowerShell window), or use a different terminal. Commands such as 'pyocd --version' are harmless; the crash follows probe-accessing commands.

## Source

Resolution: workaround

Versions: pyOCD 0.29 to 0.32 on Windows 10/11

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1129](https://github.com/pyocd/pyOCD/issues/1129), summarized in own words; confidence medium, not reviewed yet.
