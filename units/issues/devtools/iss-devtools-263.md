---
id: "iss-devtools-263"
type: "troubleshooting"
domain: "project"
title: "csolution: add-paths ignored or error when used under files or repeated as map keys"
summary: "add-paths is valid for file, group, component, project, layer and the types, but not for the files list; repeating the add-paths key in one map is invalid YAML (keys must be unique)."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/263"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/263"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

add-paths is valid for file, group, component, project, layer and the types, but not for the files list; repeating the add-paths key in one map is invalid YAML (keys must be unique).

## Fix

Put add-paths at group or project level as a list: add-paths: [., ./targets/board] or one entry per line.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #263](https://github.com/Open-CMSIS-Pack/devtools/issues/263), summarized in own words; confidence high, not reviewed yet.
