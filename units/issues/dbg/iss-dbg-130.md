---
id: "iss-dbg-130"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Debugger hangs when more breakpoints are set than hardware allows"
summary: "GDB accepts all and fails at continue with \"Command aborted\" after sending ^running; the adapter had already dropped the command."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/130"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/130"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

GDB accepts all and fails at continue with "Command aborted" after sending ^running; the adapter had already dropped the command.

## Fix

Update CDT GDB Adapter (PR 415); remove surplus breakpoints. Workaround: set breakpoint always-inserted on in initCommands.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #130](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/130), summarized in own words; confidence high, not reviewed yet.
