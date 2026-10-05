---
id: "iss-sol-313"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Create Solution fails with 'cproject not parsed, adding context failed'"
summary: "Race: the solution was loaded before all project files were written to disk."
status: "draft"
tool: "cmsis-solution"
symptoms: ["csolution error: Blank.cproject.yml - cproject file was not found", "csolution error: cproject not parsed, adding context failed"]
symptom_regex: "csolution\\s+error:\\s+Blank\\.cproject\\.yml\\s+\\-\\s+cproject\\s+file\\s+was\\s+not\\s+found"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/313"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/313"
resolution: "fixed-in-release"
versions: "1.68.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`csolution error: Blank.cproject.yml - cproject file was not found`
`csolution error: cproject not parsed, adding context failed`

## Cause

Race: the solution was loaded before all project files were written to disk.

## Fix

Fix merged after 1.68.0; try Refresh (Reload Packs, Update RTE), which did not help for the reporter.

## Source

Resolution: fixed-in-release

Versions: 1.68.0

From [Open-CMSIS-Pack/vscode-cmsis-solution #313](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/313), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
