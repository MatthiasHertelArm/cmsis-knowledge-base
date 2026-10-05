---
id: "iss-dbg-89"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: GDB server fails to start but the adapter keeps waiting for a timeout"
summary: "The adapter did not notice early exit of the GDB server."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["gdbserver has exited with code 1"]
symptom_regex: "gdbserver\\s+has\\s+exited\\s+with\\s+code\\s+\\S+"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/89"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/89"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`gdbserver has exited with code 1`

## Cause

The adapter did not notice early exit of the GDB server.

## Fix

Update CDT GDB Adapter to 2.1.0 or later; check the server error in the console.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #89](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/89), summarized in own words; confidence high, not reviewed yet.
