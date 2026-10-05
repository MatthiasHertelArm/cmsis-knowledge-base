---
id: "iss-dbg-664"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Internal pyOCD targets fail to program after double buffering was disabled"
summary: "After double buffering was disabled by default, the flash algorithms of some pyOCD internal targets used a different buffer address, so programming failed."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/664"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/664"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

After double buffering was disabled by default, the flash algorithms of some pyOCD internal targets used a different buffer address, so programming failed.

## Fix

Use a pyOCD build with PR 1898: double buffering is enabled again by default for internal targets, begin_data is replaced by a single page_buffers entry, and STM32H7xx internal targets keep only one buffer. It was tested on several boards; no release is named.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #664](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/664), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
