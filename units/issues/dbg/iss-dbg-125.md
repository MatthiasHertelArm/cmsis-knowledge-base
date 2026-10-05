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
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Double-buffered downloads stall on buses with strict timing.

## Fix

Use a pyOCD with double buffering off by default (later restored only for internal targets).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #125](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/125), summarized in own words; confidence high, not reviewed yet.
