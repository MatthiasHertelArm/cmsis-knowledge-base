---
id: "iss-sol-188"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Loading Solution never ends after modifying debug-adapters.yml"
summary: "Runtime errors while processing the debug adapter registry were not caught, so tasks and launch update never completed."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/188"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/188"
resolution: "fixed-in-release"
versions: "1.67.2"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Runtime errors while processing the debug adapter registry were not caught, so tasks and launch update never completed.

## Fix

Fixed (PR 199): the solution loads and the error is reported as a normal VS Code problem; restore the original debug-adapters.yml.

## Source

Resolution: fixed-in-release

Versions: 1.67.2

From [Open-CMSIS-Pack/vscode-cmsis-solution #188](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/188), summarized in own words; confidence medium, not reviewed yet.
