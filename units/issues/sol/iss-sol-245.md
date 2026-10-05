---
id: "iss-sol-245"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: clangd reports a header of a newly added component as not found until Rebuild all"
summary: "compile_commands.json for clangd was not refreshed after components were added."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/245"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/245"
resolution: "fixed-in-release"
versions: "1.67"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

compile_commands.json for clangd was not refreshed after components were added.

## Fix

Fixed with CMSIS-Toolbox nightly 2026-05-07 (cbuild2cmake) and the matching extension; run Rebuild all on older versions.

## Source

Resolution: fixed-in-release

Versions: 1.67

From [Open-CMSIS-Pack/vscode-cmsis-solution #245](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/245), summarized in own words; confidence high, checked against the thread, not reviewed yet.
