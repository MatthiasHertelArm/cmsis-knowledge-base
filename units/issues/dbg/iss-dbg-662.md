---
id: "iss-dbg-662"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD load crashes on flash algorithms without an RW section"
summary: "pyOCD assumed every flash algorithm has an RW section and failed on a missing section object."
status: "draft"
tool: "pyocd"
symptoms: ["C Error: 'MemoryRange' object has no attribute 'data' [__main__]"]
symptom_regex: "C\\s+Error:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/662"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/662"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Error: 'MemoryRange' object has no attribute 'data' [__main__]`

## Cause

pyOCD assumed every flash algorithm has an RW section and failed on a missing section object.

## Fix

Use a pyOCD nightly or release after December 2025 that skips absent sections.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #662](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/662), summarized in own words; confidence high, not reviewed yet.
