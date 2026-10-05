---
id: "iss-dbg-133"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Cannot read memory at peripheral register addresses with pyOCD"
summary: "GDB had no memory map entry for peripheral ranges, so reads failed."
status: "draft"
tool: "pyocd"
symptoms: ["Unable to read memory"]
symptom_regex: "Unable\\s+to\\s+read\\s+memory"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/133"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/133"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unable to read memory`

## Cause

GDB had no memory map entry for peripheral ranges, so reads failed.

## Fix

Use pyOCD patch release 0.1.1 or later (alternative: set mem inaccessible-by-default off).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #133](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/133), summarized in own words; confidence high, not reviewed yet.
