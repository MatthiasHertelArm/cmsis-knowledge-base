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
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD used incorrect HID report sizes with some CMSIS-DAP v1 probes.

## Fix

Use a pyOCD build with PR 1854 (merged into develop; confirmed on Windows and macOS with workflow artifacts, no release named). Linux does not use the hidapi backend and still failed for one reporter.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #625](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/625), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
