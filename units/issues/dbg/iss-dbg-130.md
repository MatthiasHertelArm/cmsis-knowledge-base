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
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

GDB accepts all and fails at continue with "Command aborted" after sending ^running; the adapter had already dropped the command.

## Fix

Keep the number of breakpoints within the hardware limit (an improved error message asks to remove breakpoints). A CDT GDB Adapter fix for the late error (PR 415) was implemented but still needed tests; no release is named. Possible workaround: 'set breakpoint always-inserted on' in initCommands, which however uncovers other breakpoint management issues.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #130](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/130), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
