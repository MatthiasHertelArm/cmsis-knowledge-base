---
id: "iss-dbg-595"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Live View only updates when the target is stopped (ST-Link)"
summary: "The launch configuration had auxiliaryGdb set to true, which does not work for the used server, so live reads were not possible."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/595"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/595"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The launch configuration had auxiliaryGdb set to true, which does not work for the used server, so live reads were not possible.

## Fix

Set "auxiliaryGdb": false in the launch configuration for that setup.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/vscode-cmsis-debugger #595](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/595), summarized in own words; confidence medium, not reviewed yet.
