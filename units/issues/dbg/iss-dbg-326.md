---
id: "iss-dbg-326"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Misleading error for attach request when no GDB server runs"
summary: "The adapter passed through GDB messages, which differ by OS (a drive-joining text on Windows, a timeout text on macOS)."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/326"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/326"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The adapter passed through GDB messages, which differ by OS (a drive-joining text on Windows, a timeout text on macOS).

## Fix

Update CDT GDB Adapter (PR 413 unifies the message). Start the GDB server first.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #326](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/326), summarized in own words; confidence medium, not reviewed yet.
