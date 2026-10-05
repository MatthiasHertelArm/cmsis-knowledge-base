---
id: "iss-dbg-461"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: GD-Link (CMSIS-DAP v1 without serial number) not found by pyOCD 0.38 / extension 1.0.0"
summary: "The hidapi backend regressed for CMSIS-DAP v1 probes that report no USB serial number, although pyocd list shows the probe."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/461"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/461"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["GD32"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The hidapi backend regressed for CMSIS-DAP v1 probes that report no USB serial number, although pyocd list shows the probe.

## Fix

Use a pyOCD with the fix by the CMSIS Debugger team (released after 1.0.0). To test a custom build, change the pyocd path in both launch.json and tasks.json.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #461](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/461), summarized in own words; confidence medium, not reviewed yet.
