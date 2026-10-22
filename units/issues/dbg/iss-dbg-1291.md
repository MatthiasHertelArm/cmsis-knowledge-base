---
id: "iss-dbg-1291"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Harmless 'evaluation without frameid' popups at debug startup (GDB adapter race)"
summary: "VS Code asks the debug adapter to evaluate Watch and hover expressions before any stack frame exists."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["Evaluation ... without frameid is not supported."]
symptom_regex: "Evaluation\\s+\\.\\.\\.\\s+without\\s+frameid\\s+is\\s+not\\s+supported\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1291"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1291"
resolution: "unresolved"
versions: "Seen in CMSIS Debugger 1.9.0; rescheduled target 1.12.0"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Evaluation ... without frameid is not supported.`

## Cause

VS Code asks the debug adapter to evaluate Watch and hover expressions before any stack frame exists. The CDT GDB Adapter requires a frame ID for evaluation, so it rejects these early requests. This is a timing race inside the GDB adapter, not a firmware or CMSIS Debugger fault.

## Fix

The popups can usually be ignored; the debugger still stops correctly in main(). The race is a known issue in the CDT GDB Adapter (related to #862) and was rescheduled to CMSIS Debugger 1.12.0. The thread is still open and no fix has landed.

## Source

Resolution: unresolved

Versions: Seen in CMSIS Debugger 1.9.0; rescheduled target 1.12.0

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1291](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1291), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
