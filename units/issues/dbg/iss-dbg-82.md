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
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Evaluation of expression without frameId is not supported.`

## Cause

The adapter required a frame for evaluation, which does not exist while running.

## Fix

Use CDT GDB Adapter 2.4+ with an auxiliary GDB connection (auxiliaryGdb) for running targets.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #82](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/82), summarized in own words; confidence high, not reviewed yet.
