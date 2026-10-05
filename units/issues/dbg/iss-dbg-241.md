---
id: "iss-dbg-241"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD does not use the default CMSIS_PACK_ROOT"
summary: "pyOCD only read the environment variable and ignored the documented platform default."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/241"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/241"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD only read the environment variable and ignored the documented platform default.

## Fix

Use a newer pyOCD that applies the default, or set CMSIS_PACK_ROOT.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #241](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/241), summarized in own words; confidence high, not reviewed yet.
