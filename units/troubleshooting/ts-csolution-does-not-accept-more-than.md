---
id: "ts-csolution-does-not-accept-more-than"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: component '…' does not accept more than … instance(s)"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["component '<…>' does not accept more than <…> instance(s)"]
symptom_regex: "^component '.+?' does not accept more than .+? instance\\(s\\)$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2042"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A component under components: sets `instances:` higher than its pack allows: the pack's maxInstances attribute, or 1 when the pack does not set it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2040-2047", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteItem.cpp:732-738", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6257-6283", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/Instances/instances.cproject.yml:10-12"]
---

## Symptom

`component '<…>' does not accept more than <…> instance(s)`

## Cause

A component under components: sets `instances:` higher than its pack allows: the pack's maxInstances attribute, or 1 when the pack does not set it. The `<…>` are the component and the allowed maximum.

## Fix

Lower `instances:` to the maximum or remove it (one instance is the default), or select a component variant that supports several instances.

## Trigger in the source

```cpp
if (item.instances > matchedComponentInstance->GetMaxInstances()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2040-2047`
- `libs/rtemodel/src/RteItem.cpp:732-738`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6257-6283`
- `tools/projmgr/test/data/TestSolution/Instances/instances.cproject.yml:10-12`
