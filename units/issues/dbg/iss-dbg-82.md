---
id: "iss-dbg-82"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: GDB commands in Debug Console fail while CPU runs: no frameId"
summary: "The adapter required a frame for evaluation, which does not exist while running."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["Evaluation of expression without frameId is not supported."]
symptom_regex: "Evaluation\\s+of\\s+expression\\s+without\\s+frameId\\s+is\\s+not\\s+supported\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/82"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/82"
resolution: "unresolved"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Evaluation of expression without frameId is not supported.`

## Cause

The adapter required a frame for evaluation, which does not exist while running.

## Fix

Auxiliary GDB connections were implemented in PRs (cdt-gdb-adapter 449, cdt-gdb-vscode 181) that were still open at the end of the thread; they were tested with the J-Link, ST-Link (STM32CubeIDE) and OpenOCD GDB servers, which accept several connections on one port. Use an adapter that contains them; the thread names no release.

## Source

Resolution: unresolved

From [Open-CMSIS-Pack/vscode-cmsis-debugger #82](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/82), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
