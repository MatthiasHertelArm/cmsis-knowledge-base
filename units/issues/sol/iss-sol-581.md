---
id: "iss-sol-581"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Multi-core start processor (start-pname) not selectable when device is only set in cproject.yml"
summary: "The start processor of a multi-core device is chosen from the order of the project entries."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"], "device": ["LPC55S69JBD100"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The start processor of a multi-core device is chosen from the order of the project entries. Processor names are known only when the device is given in the target-type of the csolution file; when the device is set only in the cproject file, start-pname could not be picked in Manage Solution.

## Fix

Add the device to the target-type in the csolution file, for example under the target-type's device key, so the processor names are known and start-pname can be selected. As a workaround, add start-pname under the debugger node by hand. The extension now fetches device and processor names from the generated *.cbuild.yml files, so the same selection works when only the board is given in the target-type.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #581](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
