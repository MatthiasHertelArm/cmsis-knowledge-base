---
id: "iss-dbg-345"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Custom Reset button fails with \"The custom reset command failed\" while the target runs"
summary: "GDB refuses remote commands while the CPU is running, and the adapter issued the reset without halting first."
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
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`The custom reset command failed`

## Cause

GDB refuses remote commands while the CPU is running, and the adapter issued the reset without halting first.

## Fix

Pause the target before pressing Custom Reset. The adapter was changed (PR 464) to halt first; it does not auto-resume afterwards.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #345](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/345), summarized in own words; confidence low, not reviewed yet.
