---
id: "iss-sol-30"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Loading Solution never stops when the csolution lists a project file that does not exist"
summary: "A csolution.yml that lists a project file that does not exist left the load process hanging, so Loading Solution never stopped."
status: "draft"
tool: "cmsis-solution"
symptoms: ["error csolution: unknown selected context(s):"]
symptom_regex: "unknown\\s+selected\\s+context\\(s\\):"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/30"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/30"
resolution: "fixed-in-release"
versions: "vscode-cmsis-solution 1.60.0, CMSIS-Toolbox 2.11"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: unknown selected context(s):`

## Cause

A csolution.yml that lists a project file that does not exist left the load process hanging, so Loading Solution never stopped.

## Fix

Fixed: the outline now shows 'Solution cannot be loaded' instead of Loading (validated with the CMSIS Solution nightly of 2026-03-23).

## Source

Resolution: fixed-in-release

Versions: vscode-cmsis-solution 1.60.0, CMSIS-Toolbox 2.11

From [Open-CMSIS-Pack/vscode-cmsis-solution #30](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/30), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
