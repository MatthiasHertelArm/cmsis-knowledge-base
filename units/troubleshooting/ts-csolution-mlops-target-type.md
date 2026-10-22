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
summary: "The MLOps item in the csolution YAML names a target-type that is not declared under the csolution's target-types section."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:25-33", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:59-80"]
---

## Symptom

`mlops: target type '<…>' not found`

## Cause

The MLOps item in the csolution YAML names a target-type that is not declared under the csolution's target-types section. ResolveTargetSet searches csolution.targetTypes by name, and when the requested target.targetType matches none of the declared names, FindTargetType returns false and the error is printed with the requested name substituted for the placeholder.

## Fix

Check the target-type name used by the mlops entry against the target-types declared in the csolution file and make them match exactly, since the comparison is a plain string equality. Either correct the mlops reference or add a matching target-type declaration to the csolution. If the mlops entry does not need a specific target-type, leave its target-type empty so the tool selects a declared one.

## Trigger in the source

```cpp
if (!FindTargetType(csolution, target.targetType, targetType)) {
```

## Note

The message has no code and the README does not document it. The fallback branch when the target-type is empty returns true even when no target set was found, which the source handles separately and is not part of this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:25-33`
- `tools/projmgr/src/ProjMgrMlops.cpp:59-80`
