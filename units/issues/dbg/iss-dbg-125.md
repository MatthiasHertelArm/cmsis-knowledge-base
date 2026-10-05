---
id: "iss-dbg-125"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Unreliable flash programming on STM32H7 (hard fault after load)"
summary: "Double-buffered downloads stall on buses with strict timing."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/125"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/125"
resolution: "fixed-in-release"
versions: "pyOCD v0.0.0-standalone-cbuild2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Double-buffered downloads stall on buses with strict timing.

## Fix

Use a pyOCD with double buffering disabled by default, first provided in the standalone pyOCD build v0.0.0-standalone-cbuild2.

## Source

Resolution: fixed-in-release

Versions: pyOCD v0.0.0-standalone-cbuild2

From [Open-CMSIS-Pack/vscode-cmsis-debugger #125](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/125), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
