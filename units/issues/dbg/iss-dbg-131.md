---
id: "iss-dbg-131"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CoreSight discovery fails on MEM-APs with SPROT field"
summary: "The HNONSEC bit in CSW was handled wrongly for MEM-APs that implement SPROT."
status: "draft"
tool: "pyocd"
symptoms: ["E Transfer error while reading AHB-AP#1 ROM table: Memory transfer fault @ 0xe00fefd0-0xe00fefff [ap]"]
symptom_regex: "E\\s+Transfer\\s+error\\s+while\\s+reading\\s+AHB\\-AP\\#\\S+\\s+ROM\\s+table:\\s+Memory\\s+transfer\\s+fault\\s+@\\s+\\S+\\-\\S+"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/131"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/131"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S69"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E Transfer error while reading AHB-AP#1 ROM table: Memory transfer fault @ 0xe00fefd0-0xe00fefff [ap]`

## Cause

The HNONSEC bit in CSW was handled wrongly for MEM-APs that implement SPROT.

## Fix

Use a pyOCD with the SPROT CSW handling (CMSIS Debugger 0.2 and later).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #131](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/131), summarized in own words; confidence high, not reviewed yet.
