---
id: "iss-sol-188"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Loading Solution never ends after modifying debug-adapters.yml"
summary: "A modified debug-adapters.yml led to runtime errors in processing the debug adapter registry that were apparently not caught; the maintainer assumed loading only completes once the tasks.json and launch.json update does, so loading never ended."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/188"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/188"
resolution: "fixed-in-release"
versions: "1.67.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A modified debug-adapters.yml led to runtime errors in processing the debug adapter registry that were apparently not caught; the maintainer assumed loading only completes once the tasks.json and launch.json update does, so loading never ended.

## Fix

Fixed by #199: the solution loads and the problem is reported the usual VS Code way.

## Source

Resolution: fixed-in-release

Versions: 1.67.2

From [Open-CMSIS-Pack/vscode-cmsis-solution #188](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/188), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
