---
id: "iss-sol-566"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Configuration Wizard source view jumps back to the selected node's annotation while editing"
summary: "When a node is selected in the graphical Configuration Wizard, the source editor keeps syncing its cursor and scroll position to that node's annotation."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566"
resolution: "fixed-in-release"
versions: "Validated on nightly build 2026-10-11; confirmed on nightly 1.72.1-24-20261012. No release version named."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"], "board": ["STM32H747I-EVAL"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

When a node is selected in the graphical Configuration Wizard, the source editor keeps syncing its cursor and scroll position to that node's annotation. The sync does not stop once the user moves the cursor or clicks into the source editor, so each edit pulls the view back to the annotation.

## Fix

Workaround: close the graphical Configuration Wizard view while editing the file in source mode. The intended behaviour is that the graphical-to-source sync ends once the user moves the cursor or clicks in the editor; reporters said the jumping stopped in nightly build 2026-10-11 and confirmed nightly 1.72.1-24-20261012.

## Source

Resolution: fixed-in-release

Versions: Validated on nightly build 2026-10-11; confirmed on nightly 1.72.1-24-20261012. No release version named.

From [Open-CMSIS-Pack/vscode-cmsis-solution #566](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
