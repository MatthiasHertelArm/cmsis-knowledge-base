---
id: "ts-csolution-target-types-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: target-types not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["target-types not found"]
symptom_regex: "^target\\-types not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:95"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:94", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1033", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:1256", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/missing_target_types.csolution.yml:3", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5180"]
---

## Symptom

`target-types not found`

## Cause

The csolution.yml defines no usable target type: `target-types:` is missing or empty, or a `type:` name contains `.` or `+`, in which case an `invalid target type(s)` error lists those names first. The schema check also demands `target-types:`, so the bare message appears mainly with `-n`.

## Fix

Add at least one target type with a name made of letters, digits, `_` and `-`, e.g. `target-types:` - `type: CM0` with `device: ARMCM0`; rename types that contain `.` or `+`.

## Trigger in the source

```cpp
if (!ParseTargetTypes(solutionNode, csolution.path, csolution.targetTypes)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:94`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1033`
- `tools/projmgr/schemas/common.schema.json:1256`
- `tools/projmgr/test/data/TestSolution/missing_target_types.csolution.yml:3`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5180`
