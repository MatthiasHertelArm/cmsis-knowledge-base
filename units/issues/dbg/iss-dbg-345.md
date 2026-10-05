---
id: "iss-dbg-345"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Custom Reset button fails with \"The custom reset command failed\" while the target runs"
summary: "Custom Reset failed while the target was running; the maintainers tied it to the missing non-stop mode support."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["The custom reset command failed"]
symptom_regex: "The\\s+custom\\s+reset\\s+command\\s+failed"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/345"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/345"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`The custom reset command failed`

## Cause

Custom Reset failed while the target was running; the maintainers tied it to the missing non-stop mode support.

## Fix

Pause the target before pressing Custom Reset. A CDT GDB Adapter change that halts the target before the reset (PR 464) was still in review at the end of the thread; it would not resume execution afterwards unless the customResetCommands do so.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #345](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/345), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
