---
id: "ts-csolution-mlops-target-type"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops: target type '…' not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: target type '<…>' not found"]
symptom_regex: "^mlops: target type '.+?' not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrMlops.cpp:78"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`mlops:` - `hardware:` or `simulator:` - `target:` names a target type that is not declared under `target-types:` in the csolution.yml; `<…>` is that name (the part before `@`)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:25", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:76", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7989"]
---

## Symptom

`mlops: target type '<…>' not found`

## Cause

`mlops:` - `hardware:` or `simulator:` - `target:` names a target type that is not declared under `target-types:` in the csolution.yml; `<…>` is that name (the part before `@`).

## Fix

Use the `type:` of an existing target type in `target: <type>[@<set>]`, or add that target type under `target-types:`.

## Trigger in the source

```cpp
if (!FindTargetType(csolution, target.targetType, targetType)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:25`
- `tools/projmgr/src/ProjMgrMlops.cpp:76`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7989`
