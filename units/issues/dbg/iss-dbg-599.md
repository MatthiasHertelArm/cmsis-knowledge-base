---
id: "iss-dbg-599"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: XRTOS view stuck on \"Loading\" with Zephyr"
summary: "RTOS Views 0.0.12 changed Zephyr thread state names and did not work with the Zephyr examples."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/599"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/599"
resolution: "fixed-in-release"
versions: "RTOS Views 0.0.12 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

RTOS Views 0.0.12 changed Zephyr thread state names and did not work with the Zephyr examples.

## Fix

Install RTOS Views 0.0.13 or later.

## Source

Resolution: fixed-in-release

Versions: RTOS Views 0.0.12 affected

From [Open-CMSIS-Pack/vscode-cmsis-debugger #599](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/599), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
