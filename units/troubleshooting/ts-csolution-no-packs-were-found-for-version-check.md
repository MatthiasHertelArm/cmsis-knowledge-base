---
id: "ts-csolution-no-packs-were-found-for-version-check"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no packs were found for version check"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no packs were found for version check"]
symptom_regex: "^no packs were found for version check$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:6202"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The version check builds a list of results from the packs loaded for the selected contexts (usedPacks, filled from m_loadedPacks in the loop at lines 6150-6167)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6150-6167", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6169-6172", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6201-6204"]
---

## Symptom

`no packs were found for version check`

## Cause

The version check builds a list of results from the packs loaded for the selected contexts (usedPacks, filled from m_loadedPacks in the loop at lines 6150-6167). When no packs were loaded for any selected context, usedPacks stays empty, checkPackResults stays empty, and the tool prints this error and returns false. This means the project's selected contexts resolved to no packs, so there was nothing to compare against the latest installed versions.

## Fix

Check that the csolution project lists the packs it uses (for example through its components or pack requirements) and that those packs are installed in the CMSIS pack root or in a project-specified pack path. Then rerun the version check on the same project. The source does not show which user input leads to an empty pack list, so verify the pack list for the context you run it on.

## Trigger in the source

```cpp
if (checkPackResults.empty()) {
```

## Note

The README does not document this message. The source shows the trigger as an empty result list, but not which project input causes the list to be empty, so the cause is an inference from the code. The message without a filter is distinct from the filtered variant at line 6209, which adds the filter text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6150-6167`
- `tools/projmgr/src/ProjMgrWorker.cpp:6169-6172`
- `tools/projmgr/src/ProjMgrWorker.cpp:6201-6204`
