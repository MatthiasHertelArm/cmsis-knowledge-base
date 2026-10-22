---
id: "iss-sol-566"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Configuration Wizard source editor jumps back to the selected node's annotation while editing"
summary: "The Configuration Wizard keeps syncing the source editor's cursor and scroll position to the annotation of the last node selected in the graphical view."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566"
resolution: "workaround"
versions: "Validated on nightly build 2026-10-11; confirmed on nightly 1.72.1-24-20261012."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["vscode-cmsis-solution"], "component": ["Configuration Wizard"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Configuration Wizard keeps syncing the source editor's cursor and scroll position to the annotation of the last node selected in the graphical view. The sync does not end once the user starts editing in the source view, so the editor moves back on each pause or save.

## Fix

Workaround: close the graphical Configuration Wizard view while editing the file in source mode. Nightly build 2026-10-11 was validated as no longer showing the jumps, and nightly 1.72.1-24-20261012 was also confirmed.

## Source

Resolution: workaround

Versions: Validated on nightly build 2026-10-11; confirmed on nightly 1.72.1-24-20261012.

From [Open-CMSIS-Pack/vscode-cmsis-solution #566](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
