---
id: "iss-dbg-566"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Noisy \"Selected thread is running\" and \"stream was destroyed\" errors in Debug Console"
summary: "Views send requests while the target changes state (step/run, disconnect), and the adapter surfaced the resulting internal errors to the user."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["Selected thread is running", "Cannot call write after a stream was destroyed"]
symptom_regex: "Selected\\s+thread\\s+is\\s+running"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/566"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/566"
resolution: "fixed-in-release"
versions: "fixed in CDT GDB Adapter 2.6.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Selected thread is running`
`Cannot call write after a stream was destroyed`

## Cause

Views send requests while the target changes state (step/run, disconnect), and the adapter surfaced the resulting internal errors to the user.

## Fix

Update CDT GDB Adapter to 2.6.0 or later. The related AC6 "not in symtab" warnings come from reading osRtxConfig.

## Source

Resolution: fixed-in-release

Versions: fixed in CDT GDB Adapter 2.6.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #566](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/566), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
