---
id: "iss-dbg-812"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: \"No view is registered with id: cmsis-debugger.componentViewer\" after extension update"
summary: "After updating from a release without Component Viewer to one with it, and only restarting extensions, VS Code has not registered the new view container."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["No view is registered with id: cmsis-debugger.componentViewer"]
symptom_regex: "No\\s+view\\s+is\\s+registered\\s+with\\s+id:\\s+cmsis\\-debugger\\.componentViewer"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/812"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/812"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No view is registered with id: cmsis-debugger.componentViewer`

## Cause

After updating from a release without Component Viewer to one with it, and only restarting extensions, VS Code has not registered the new view container.

## Fix

Reload or restart the VS Code window after the update. Newer versions show a warning with a Reload Window button when they detect this state.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #812](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/812), summarized in own words; confidence high, not reviewed yet.
