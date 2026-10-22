---
id: "ts-csolution-is-listed-multiple-times"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: component '…' is listed multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: component '<…>' is listed multiple times"]
symptom_regex: "^conflict: component '.+?' is listed multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3909"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "AddComponent appends each component to the destination list only if no entry with the same component name is already there."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3900-3901", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3903-3910", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3913"]
---

## Symptom

`conflict: component '<…>' is listed multiple times`

## Cause

AddComponent appends each component to the destination list only if no entry with the same component name is already there. When it finds a match and the caller did not set ignoreDuplicates, it logs this error and returns false. So the same component name (the '<…>' in the message) was collected twice for one context, for example through two component entries in the csolution project or through a layer that repeats a component already listed in the project. The lines given do not show the callers, so which input path produced the second entry is not confirmed.

## Fix

Find every place the named component is added for this context (the components list in the .csolution.yml or the .cproject.yml, and any clayer that declares it) and keep only one entry. If the same component has to come from several sources, give each entry a distinct filter so only one applies to a given context. Then rerun the csolution command.

## Trigger in the source

```cpp
if (ignoreDuplicates) {
```

## Note

The message is not documented in the README. The code is empty in the message. The ignoreDuplicates path prints a warning ('ignoring conflict') instead of this error, so the callers that pass true decide whether users see the error at all; those callers are outside the lines given. The fix above is a reading of the trigger and is not confirmed by a README entry.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3900-3901`
- `tools/projmgr/src/ProjMgrWorker.cpp:3903-3910`
- `tools/projmgr/src/ProjMgrWorker.cpp:3913`
