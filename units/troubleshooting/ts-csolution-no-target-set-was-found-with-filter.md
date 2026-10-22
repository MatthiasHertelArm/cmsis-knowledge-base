---
id: "ts-csolution-no-target-set-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no target-set was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no target-set was found with filter '<…>'"]
symptom_regex: "^no target\\-set was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4869"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution command was given a filter (for listing target-sets) and none of the target-set names built from the csolution's target-types match it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4856-4877", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4859-4863", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4865-4871"]
---

## Symptom

`no target-set was found with filter '<…>'`

## Cause

The csolution command was given a filter (for listing target-sets) and none of the target-set names built from the csolution's target-types match it. Each target-set is listed as its target-type name, with '@' and the set name appended when the set is non-empty, and the filter is matched against these names with RteUtils::ApplyFilter. The '<…>' in the message is the filter text as the user passed it.

## Fix

Check the target-type and target-set names defined in the csolution.yml under target-types, then rerun the listing with a filter that matches them, for example the bare target-type name or name@set. Omit the filter to list all target-sets.

## Trigger in the source

```cpp
if (filteredTargetSets.empty()) {
```

## Note

The message is not listed in the README. The sibling message for contexts ('no context was found with filter') uses the same pattern at ProjMgrWorker.cpp:4843; this entry covers only the target-set listing path.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4856-4877`
- `tools/projmgr/src/ProjMgrWorker.cpp:4859-4863`
- `tools/projmgr/src/ProjMgrWorker.cpp:4865-4871`
