---
id: "ts-csolution-redefinition-from-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefinition from '…' into '…'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["redefinition from '<…>' into '<…>'"]
symptom_regex: "^redefinition from '.+?' into '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3005"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProcessCompilerPrecedence found that the compiler value already assigned (the first '<…>') is not compatible with a compiler value coming from another layer or item (the second '<…>'), and the caller passed acceptRedefinition set to true."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3000-3011", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3004-3006"]
---

## Symptom

`redefinition from '<…>' into '<…>'`

## Cause

ProcessCompilerPrecedence found that the compiler value already assigned (the first '<…>') is not compatible with a compiler value coming from another layer or item (the second '<…>'), and the caller passed acceptRedefinition set to true. The check compares the compilers with ProjMgrUtils::AreCompilersCompatible; when they differ, the new value overwrites the old one and the warning is logged. Typical sources are compiler settings that differ between the csolution, the project, a target type or build type, and a layer.

## Fix

Make the compiler setting identical everywhere it is defined in the csolution and project YAML files (the compiler key under the target or build type, the project and the layers), so that the values are compatible and no overwrite happens. If the overwrite is unintended, remove or align the conflicting compiler entry; the warning itself does not stop the build.

## Trigger in the source

```cpp
if (acceptRedefinition) {
```

## Note

Only the warning branch is shown in the trigger; the error variant with 'is not allowed' at line 3008 is the strict case when acceptRedefinition is false. Which callers pass acceptRedefinition as true is outside the lines given, so the exact user-facing configuration that leads there is inferred from the compiler precedence comments and the check, not confirmed. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3000-3011`
- `tools/projmgr/src/ProjMgrWorker.cpp:3004-3006`
