---
id: "iss-dbg-645"
type: "troubleshooting"
domain: "debug"
title: "GDB: GDB warning \"unable to determine psp alias, assuming psp_s\" during Zephyr debug"
summary: "pyOCD Zephyr thread awareness does not model Secure and Non-secure state, so GDB cannot tell which PSP alias belongs to a paused thread."
status: "draft"
tool: "gdb"
symptoms: ["warning: Invalid state, unable to determine psp alias, assuming psp_s."]
symptom_regex: "Invalid\\s+state,\\s+unable\\s+to\\s+determine\\s+psp\\s+alias,\\s+assuming\\s+psp_s\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/645"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/645"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["gdb"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning: Invalid state, unable to determine psp alias, assuming psp_s.`

## Cause

pyOCD Zephyr thread awareness does not model Secure and Non-secure state, so GDB cannot tell which PSP alias belongs to a paused thread.

## Fix

Ignore it: only the PSP/MSP alias register values of paused threads may be wrong. The unrelated "pc ... in read in CU" warning has the same harmless nature.

## Source

Resolution: not-a-bug

From [Open-CMSIS-Pack/vscode-cmsis-debugger #645](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/645), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
