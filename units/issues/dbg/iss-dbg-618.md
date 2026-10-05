---
id: "iss-dbg-618"
type: "troubleshooting"
domain: "general"
title: "other: Debug of Alif DevKit-E8 with CMSIS-DAP fails"
summary: "The reset sequences in the Alif DFP 2.0.x were broken, and the device additionally had to be provisioned with the Alif security tools."
status: "draft"
tool: "other"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/618"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/618"
resolution: "fixed-in-release"
versions: "DFP 2.0.2 to 2.0.4 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["Alif DevKit-E8"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The reset sequences in the Alif DFP 2.0.x were broken, and the device additionally had to be provisioned with the Alif security tools.

## Fix

Use Alif DFP 2.1.0 or later, a current CMSIS-Toolbox, and provision the device with the Alif SE tools when switching cores.

## Source

Resolution: fixed-in-release

Versions: DFP 2.0.2 to 2.0.4 affected

From [Open-CMSIS-Pack/vscode-cmsis-debugger #618](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/618), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
