---
id: "iss-sol-581"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Manage Solution lacks start processor selection on multi-core target when device is missing"
summary: "The extension only offered a start processor choice when the device was set in the target-type."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["vscode-cmsis-solution"], "device": ["LPC55S69JBD100"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The extension only offered a start processor choice when the device was set in the target-type. When the device was given only in the project file, the start processor was chosen implicitly from the order of the project files.

## Fix

Add the device to the target-type in the solution file so the start processor can be selected, or add start-pname under the debugger node by hand. The later fix reads device and processor names from the generated cbuild.yml files, so selection also works when the device is set only in the project file.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #581](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
