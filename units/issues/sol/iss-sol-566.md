---
id: "iss-sol-566"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Configuration Wizard source view cursor jumps back while editing a dbgconf file"
summary: "When a node in the Configuration Wizard graphical view is selected, the source editor is synced to that node's annotation location."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566"
resolution: "workaround"
versions: "nightly build 2026-10-11; nightly 1.72.1-24-20261012"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"], "board": ["STM32H747I-EVAL"], "component": ["CoreSight trace options"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

When a node in the Configuration Wizard graphical view is selected, the source editor is synced to that node's annotation location. This sync keeps running while the user edits in source mode, so pauses in typing or saving move the scroll position and cursor back to the selected node's annotation.

## Fix

Workaround: close the graphical view until the edits in the source view are done. The maintainer's expectation is that the cursor sync from the graphical view ends once the user moves the cursor or clicks into the source editor. Nightly build 2026-10-11 was validated as no longer showing the jumps, and nightly 1.72.1-24-20261012 was confirmed.

## Source

Resolution: workaround

Versions: nightly build 2026-10-11; nightly 1.72.1-24-20261012

From [Open-CMSIS-Pack/vscode-cmsis-solution #566](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/566), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
