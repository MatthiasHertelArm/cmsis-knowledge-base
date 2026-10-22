---
id: "ts-csolution-ignoring-conflict-component"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: ignoring conflict: component '…' is listed multiple times"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["ignoring conflict: component '<…>' is listed multiple times"]
symptom_regex: "^ignoring conflict: component '.+?' is listed multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3906"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "AddComponent found a component already in the destination list for the same context, with the same component identifier as the new entry."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3900-3901", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3904-3907", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3909-3910"]
---

## Symptom

`ignoring conflict: component '<…>' is listed multiple times`

## Cause

AddComponent found a component already in the destination list for the same context, with the same component identifier as the new entry. The caller passed ignoreDuplicates as true, so the tool keeps the earlier entry, skips the new one and prints the warning. The '<…>' is the component identifier string (the component's Cclass::Cgroup form) that is listed more than once. The source does not show which caller sets ignoreDuplicates or which input file produced the second listing.

## Fix

Open the csolution or project file that lists the component and remove the duplicate entry so that each component appears once in the components list for that context. Then rerun the csolution command and check that the warning is gone. If the same component is required through several layers or dependencies, check that only one of them adds it explicitly.

## Trigger in the source

```cpp
if (ignoreDuplicates) {
```

## Note

The same duplicate condition without ignoreDuplicates prints the error 'conflict: component ... is listed multiple times' and fails. The warning is therefore the lenient variant, and the build continues with the first entry. The message has no code. The README does not document this message. The callers that pass ignoreDuplicates were not in the given lines, so which context or input triggers it is not confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3900-3901`
- `tools/projmgr/src/ProjMgrWorker.cpp:3904-3907`
- `tools/projmgr/src/ProjMgrWorker.cpp:3909-3910`
