---
id: "iss-sol-27"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Browse for UV4.exe in Manage Solution inserts a relative path and launching uVision fails"
summary: "The relative path was passed unresolved to the shell task."
status: "draft"
tool: "cmsis-solution"
symptoms: ["'..' is not recognized as an internal or external command,"]
symptom_regex: "'.*?'\\s+is\\s+not\\s+recognized\\s+as\\s+an\\s+internal\\s+or\\s+external\\s+command,"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/27"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/27"
resolution: "fixed-in-release"
versions: "1.66.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`'..' is not recognized as an internal or external command,`

## Cause

The relative path was passed unresolved to the shell task.

## Fix

Fixed in nightly 1.66.1-32; enter an absolute path on older versions.

## Source

Resolution: fixed-in-release

Versions: 1.66.0

From [Open-CMSIS-Pack/vscode-cmsis-solution #27](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/27), summarized in own words; confidence high, checked against the thread, not reviewed yet.
