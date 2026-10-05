---
id: "iss-dbg-595"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Live View only updates when the target is stopped (ST-Link)"
summary: "A faulty \"true\" value of the auxiliaryGdb setting in the launch configuration; the thread does not say what exactly was wrong with it."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/595"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/595"
resolution: "configuration"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A faulty "true" value of the auxiliaryGdb setting in the launch configuration; the thread does not say what exactly was wrong with it.

## Fix

Check the auxiliaryGdb entry in the launch configuration; once it was corrected, Live View also updated while running with ST-Link. The thread does not give the corrected value.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/vscode-cmsis-debugger #595](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/595), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
