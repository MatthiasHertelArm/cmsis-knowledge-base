---
id: "iss-dbg-628"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Breakpoints cannot be set in assembler files"
summary: "Breakpoints could not be set in assembler files because the CDT GDB Adapter extension declared no language for them; a pseudo-language definition in that extension enables them."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/628"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/628"
resolution: "fixed-in-release"
versions: "CDT GDB Adapter 2.5.0 (presumed)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Breakpoints could not be set in assembler files because the CDT GDB Adapter extension declared no language for them; a pseudo-language definition in that extension enables them.

## Fix

Use a CDT GDB Adapter release that contains the merged pseudo-language definition for assembler (cdt-gdb-vscode PR 191); it was announced for the next release, presumably 2.5.0.

## Source

Resolution: fixed-in-release

Versions: CDT GDB Adapter 2.5.0 (presumed)

From [Open-CMSIS-Pack/vscode-cmsis-debugger #628](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/628), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
