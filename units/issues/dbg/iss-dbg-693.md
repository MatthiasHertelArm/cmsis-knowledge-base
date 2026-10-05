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
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The flash algorithm path from the PDSC was used without normalization, so paths such as Pack/../other/Flash/x.FLM could not be opened.

## Fix

Use a pyOCD build with PR 1867, which was merged into the develop branch; no release is named.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #693](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/693), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
