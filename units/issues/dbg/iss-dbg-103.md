---
id: "iss-dbg-103"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Target stays halted after disconnect with pyOCD"
summary: "The adapter killed the GDB server immediately, before pyOCD could turn off debug and resume the CPU."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/103"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/103"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The adapter killed the GDB server immediately, before pyOCD could turn off debug and resume the CPU.

## Fix

Use CDT GDB Adapter with a server kill delay (PRs 405/175); keep automaticallyKillServer.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #103](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/103), summarized in own words; confidence high, not reviewed yet.
