---
id: "iss-dbg-86"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Hover shows \"-var-create: unable to create variable object\" for non-variables"
summary: "Hovering text that is no variable made the adapter report the GDB error."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["-var-create: unable to create variable object"]
symptom_regex: "\\-var\\-create:\\s+unable\\s+to\\s+create\\s+variable\\s+object"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/86"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/86"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`-var-create: unable to create variable object`

## Cause

Hovering text that is no variable made the adapter report the GDB error.

## Fix

Update CDT GDB Adapter to 2.0.4 or later.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #86](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/86), summarized in own words; confidence high, not reviewed yet.
