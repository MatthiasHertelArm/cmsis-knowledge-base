---
id: "iss-dbg-625"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v1 probe initialisation fails because of wrong HID report size handling"
summary: "pyOCD used incorrect HID report sizes with some CMSIS-DAP v1 probes."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/625"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/625"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD used incorrect HID report sizes with some CMSIS-DAP v1 probes.

## Fix

Use a pyOCD with PR 1854 (verified on Windows and macOS; the Linux backend is not hidapi and unchanged).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #625](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/625), summarized in own words; confidence high, not reviewed yet.
