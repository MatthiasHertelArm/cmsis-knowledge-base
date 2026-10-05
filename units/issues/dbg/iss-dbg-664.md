---
id: "iss-dbg-664"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Internal pyOCD targets fail to program after double buffering was disabled"
summary: "Disabling double buffering changed the buffer address the algorithm uses, and algorithms of some internal targets relied on the old begin_data location."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/664"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/664"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Disabling double buffering changed the buffer address the algorithm uses, and algorithms of some internal targets relied on the old begin_data location.

## Fix

Use a pyOCD containing PR 1898 (double buffering kept for internal targets, page_buffers cleaned up, STM32H7 excluded).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #664](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/664), summarized in own words; confidence medium, not reviewed yet.
