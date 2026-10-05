---
id: "iss-dbg-628"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Breakpoints cannot be set in assembler files"
summary: "VS Code only allows breakpoints for languages that a debug extension declares; assembler was not declared."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/628"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/628"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

VS Code only allows breakpoints for languages that a debug extension declares; assembler was not declared.

## Fix

Update the CDT GDB Adapter extension to 2.5.0 or later, which contributes the assembler language entry.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #628](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/628), summarized in own words; confidence high, not reviewed yet.
