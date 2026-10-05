---
id: "iss-dbg-165"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Typing GDB commands in the Debug Console gives var-create errors"
summary: "The Debug Console treats input as expressions; the CDT GDB Adapter takes GDB CLI commands only with a \">\" prefix."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/165"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/165"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Debug Console treats input as expressions; the CDT GDB Adapter takes GDB CLI commands only with a ">" prefix.

## Fix

Start the command with ">" for example "> help".

## Source

Resolution: user-error

From [Open-CMSIS-Pack/vscode-cmsis-debugger #165](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/165), summarized in own words; confidence high, checked against the thread, not reviewed yet.
