---
id: "iss-dbg-68"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: \"GDB unhandled notify: breakpoint-created\" for breakpoints set from the console"
summary: "The adapter did not handle GDB breakpoint notifications, so CLI breakpoints did not show in the GUI."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["GDB unhandled notify: breakpoint-created"]
symptom_regex: "GDB\\s+unhandled\\s+notify:\\s+breakpoint\\-created"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/68"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/68"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`GDB unhandled notify: breakpoint-created`

## Cause

The adapter did not handle GDB breakpoint notifications, so CLI breakpoints did not show in the GUI.

## Fix

Use a CDT GDB Adapter extension release that handles the breakpoint-created notification; the thread announces it for the next release without naming a version.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #68](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/68), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
