---
id: "iss-pyocd-1129"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PowerShell window closes after pyocd list, flash or reset on Windows"
summary: "PowerShell itself crashes: its console key reader (PSConsoleReadLine.ReadKey) throws ArgumentOutOfRangeException a moment after commands such as pyocd list, json or reset return."
status: "draft"
tool: "pyocd"
symptoms: ["Unhandled exception. System.ArgumentOutOfRangeException: Console key values must be between 0 and 255 inclusive. (Parameter 'key')"]
symptom_regex: "Unhandled\\s+exception\\.\\s+System\\.ArgumentOutOfRangeException:\\s+Console\\s+key\\s+values\\s+must\\s+be\\s+between\\s+\\S+\\s+and\\s+\\S+\\s+inclusive\\.\\s+\\(Parameter\\s+'.*?'\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1129"
doc_source: "https://github.com/pyocd/pyOCD/issues/1129"
resolution: "workaround"
versions: "pyOCD 0.29.0 to 0.32.1; Windows PowerShell 5.1, PowerShell 7.2"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unhandled exception. System.ArgumentOutOfRangeException: Console key values must be between 0 and 255 inclusive. (Parameter 'key')`

## Cause

PowerShell itself crashes: its console key reader (PSConsoleReadLine.ReadKey) throws ArgumentOutOfRangeException a moment after commands such as pyocd list, json or reset return. Seen with Windows PowerShell 5.1 and PowerShell 7.2, not with cmd.exe.

## Fix

Run pyocd from cmd.exe (this also works inside a PowerShell window). pyocd --version and the interactive pyocd commander do not trigger it.

## Source

Resolution: workaround

Versions: pyOCD 0.29.0 to 0.32.1; Windows PowerShell 5.1, PowerShell 7.2

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1129](https://github.com/pyocd/pyOCD/issues/1129), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
