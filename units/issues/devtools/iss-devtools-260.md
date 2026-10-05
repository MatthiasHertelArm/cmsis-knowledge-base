---
id: "iss-devtools-260"
type: "troubleshooting"
domain: "project"
title: "csolution: yaml-cpp error: end of map not found when add-paths is placed next to files"
summary: "add-paths was indented as a sibling of the file items inside the files sequence, which breaks the YAML structure."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: yaml-cpp: error at line 26, column 9: end of map not found"]
symptom_regex: "yaml\\-cpp:\\s+error\\s+at\\s+line\\s+\\S+,\\s+column\\s+\\S+:\\s+end\\s+of\\s+map\\s+not\\s+found"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/260"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/260"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: yaml-cpp: error at line 26, column 9: end of map not found`

## Cause

add-paths was indented as a sibling of the file items inside the files sequence, which breaks the YAML structure.

## Fix

Put add-paths under the individual file entry or at group level, with correct indentation.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #260](https://github.com/Open-CMSIS-Pack/devtools/issues/260), summarized in own words; confidence high, checked against the thread, not reviewed yet.
