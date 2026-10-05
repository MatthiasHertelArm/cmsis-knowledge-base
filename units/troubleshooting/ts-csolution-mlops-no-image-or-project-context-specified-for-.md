---
id: "ts-csolution-mlops-no-image-or-project-context-specified-for-"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops: no image or project-context specified for target '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: no image or project-context specified for target '<…>'"]
symptom_regex: "^mlops: no image or project\\-context specified for target '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:201"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:170", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:201", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/MLOps/failure3.csolution.yml:6", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7991"]
---

## Symptom

`mlops: no image or project-context specified for target '<…>'`

## Cause

`mlops:` - `hardware:` or `simulator:` - `target:` selects a target set whose `images:` list has no `project-context:` that names a project of the solution, so there is no context to build or run for that target. `<…>` is the target. Example: `images:` - `project-context: wrong_context`.

## Fix

In that target set add or correct an `images:` entry so that `project-context:` names a project from `projects:` in the csolution.yml, e.g. `- project-context: core0`.

## Trigger in the source

```cpp
if (!t.targetType.empty() && ref.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:170`
- `tools/projmgr/src/ProjMgrMlops.cpp:201`
- `tools/projmgr/test/data/MLOps/failure3.csolution.yml:6`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7991`
