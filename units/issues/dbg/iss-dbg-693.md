---
id: "iss-dbg-693"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD internal pack support fails when an algorithm path contains \"..\""
summary: "The flash algorithm path from the PDSC was used without normalization, so paths such as Pack/../other/Flash/x.FLM could not be opened."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/693"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/693"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The flash algorithm path from the PDSC was used without normalization, so paths such as Pack/../other/Flash/x.FLM could not be opened.

## Fix

Use a pyOCD with the normalization fix (PR 1867, merged into develop in December 2025).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #693](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/693), summarized in own words; confidence high, not reviewed yet.
