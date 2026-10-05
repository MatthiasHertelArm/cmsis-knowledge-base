---
id: "iss-dbg-461"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: GD-Link (CMSIS-DAP v1 without serial number) not found by pyOCD 0.38 / extension 1.0.0"
summary: "A regression in pyOCD's hidapi backend broke CMSIS-DAP v1 probes that report no USB serial number, such as the GD-Link, although 'pyocd list' shows the probe; extension 0.5.0 still worked."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/461"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/461"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["GD32"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A regression in pyOCD's hidapi backend broke CMSIS-DAP v1 probes that report no USB serial number, such as the GD-Link, although 'pyocd list' shows the probe; extension 0.5.0 still worked.

## Fix

Use a pyOCD build with the hidapi fix from the CMSIS Debugger team (the reporter verified a test build). To try a custom pyOCD in the extension, change its path in launch.json and in every pyocd entry of tasks.json.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #461](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/461), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
