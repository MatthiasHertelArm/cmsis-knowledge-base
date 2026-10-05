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
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The adapter killed the GDB server immediately, before pyOCD could turn off debug and resume the CPU.

## Fix

Use a CDT GDB Adapter with the server kill delay (PRs 405 and 175), which together with automaticallyKillServer gives pyOCD time to disconnect cleanly; it was tested with a not yet public build, no release named. Until then, reset or power-cycle the board after disconnecting.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #103](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/103), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
