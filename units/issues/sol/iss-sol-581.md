---
id: "iss-sol-581"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Start processor not selectable in Manage Solution for multi-core target with device only in project"
summary: "The start processor (start-pname) was set automatically from the order of the cproject.yml entries, so the first one became the start processor."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["VS Code CMSIS Solution"], "device": ["LPC55S69JBD100"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The start processor (start-pname) was set automatically from the order of the cproject.yml entries, so the first one became the start processor. It was not selectable when the device was specified only in cproject.yml and not in the target-type.

## Fix

Workaround: add start-pname manually under the debugger node, or add a device entry under the target-type in the csolution file, which makes the start processor selectable. The maintainers later changed the extension to read device and processor names from the generated *.cbuild.yml files, so the start processor becomes selectable without editing the target-type.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #581](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/581), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
