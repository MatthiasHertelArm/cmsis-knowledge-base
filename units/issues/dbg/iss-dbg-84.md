---
id: "iss-dbg-84"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Connect fails with cbuild-run when CMSIS_PACK_ROOT is not set"
summary: "The pack-based support needed CMSIS_PACK_ROOT and the default was not applied."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/84"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/84"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The pack-based support needed CMSIS_PACK_ROOT and the default was not applied.

## Fix

Set CMSIS_PACK_ROOT or use a version that applies defaults (see the toolbox default locations).

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #84](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/84), summarized in own words; confidence medium, not reviewed yet.
