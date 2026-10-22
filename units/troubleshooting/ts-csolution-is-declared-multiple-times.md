---
id: "ts-csolution-is-declared-multiple-times"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: group '…' is declared multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: group '<…>' is declared multiple times"]
symptom_regex: "^conflict: group '.+?' is declared multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3835"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "AddGroup compares each group in the destination list with the incoming group by its name (dstNode.group == src.group) among the groups already added at the same level."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3833-3837", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3819-3823", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3801-3815"]
---

## Symptom

`conflict: group '<…>' is declared multiple times`

## Cause

AddGroup compares each group in the destination list with the incoming group by its name (dstNode.group == src.group) among the groups already added at the same level. Two groups with the same name appear at the same nesting level of the project: the cproject groups, the clayer groups, or the groups nested inside one group, since each level is checked against its own list. The name in the message is the duplicated group name.

## Fix

Find every group with that name in the csolution project and its clayers and nested groups, then rename one of them or merge their files into a single group entry so each group name is unique at its level.

## Trigger in the source

```cpp
if (dstNode.group == src.group) {
```

## Note

The message is printed with the group name, not the file path. The check runs only for groups whose filters and compiler match the context, so a duplicate under a non-matching condition is not reported. The README has no entry for this message, so the cause above is read from the source only.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3833-3837`
- `tools/projmgr/src/ProjMgrWorker.cpp:3819-3823`
- `tools/projmgr/src/ProjMgrWorker.cpp:3801-3815`
