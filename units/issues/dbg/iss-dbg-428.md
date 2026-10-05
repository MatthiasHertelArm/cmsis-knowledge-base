---
id: "iss-dbg-428"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: PERIPHERALS view missing when attaching to a GDB server started by Load & Run"
summary: "The attach launch configuration did not pass the cbuild-run file, so the SVD path was not found."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/428"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/428"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The attach launch configuration did not pass the cbuild-run file, so the SVD path was not found.

## Fix

Use CMSIS Debugger 1.0.0 or later with CMSIS Solution templates that add cmsis/cbuildRunFile to attach configurations; or add that setting manually.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #428](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/428), summarized in own words; confidence high, not reviewed yet.
