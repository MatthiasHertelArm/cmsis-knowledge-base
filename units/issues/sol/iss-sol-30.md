---
id: "iss-sol-30"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Loading Solution never stops when the csolution lists a project file that does not exist"
summary: "The missing cproject.yml left the load process hanging."
status: "draft"
tool: "cmsis-solution"
symptoms: ["error csolution: unknown selected context(s):"]
symptom_regex: "unknown\\s+selected\\s+context\\(s\\):"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/30"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/30"
resolution: "fixed-in-release"
versions: "1.60.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: unknown selected context(s):`

## Cause

The missing cproject.yml left the load process hanging.

## Fix

Fixed in nightly of 2026-03-23: the outline shows 'Solution cannot be loaded'; correct the project path in the csolution.yml.

## Source

Resolution: fixed-in-release

Versions: 1.60.0

From [Open-CMSIS-Pack/vscode-cmsis-solution #30](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/30), summarized in own words; confidence medium, not reviewed yet.
