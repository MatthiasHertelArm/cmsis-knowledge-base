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
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The pack-based support needed CMSIS_PACK_ROOT and the default was not applied.

## Fix

Set CMSIS_PACK_ROOT; the default locations per platform are documented in the CMSIS-Toolbox installation guide. Having the extension set the default when the variable is missing was proposed, not shown as done.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #84](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/84), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
