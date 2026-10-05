---
id: "iss-dbg-386"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Erase device fails on STM32 dual-core boards"
summary: "The memory region lookup ignored the pname attribute, so it picked the wrong core region."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/386"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/386"
resolution: "fixed-in-release"
versions: "fixed in pyOCD 0.40.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32H745", "STM32H747"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The memory region lookup ignored the pname attribute, so it picked the wrong core region.

## Fix

Use pyOCD 0.40.0 or later.

## Source

Resolution: fixed-in-release

Versions: fixed in pyOCD 0.40.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #386](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/386), summarized in own words; confidence high, not reviewed yet.
