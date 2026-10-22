---
id: "ts-csolution-redefined-from"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: variable '…' redefined from '…' to '…'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["variable '<…>' redefined from '<…>' to '<…>'"]
symptom_regex: "^variable '.+?' redefined from '.+?' to '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:284"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ParseContextLayers copies user variables into context.variables in three scopes, in this order: the target build variables, the build-type variables and the target-type variables."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:238-242", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:272-288", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:283-284"]
---

## Symptom

`variable '<…>' redefined from '<…>' to '<…>'`

## Cause

ParseContextLayers copies user variables into context.variables in three scopes, in this order: the target build variables, the build-type variables and the target-type variables. Before that, ProjMgrWorker seeds the same map with built-in variables (solution, project, build type, target type and target set). The warning fires when a key is already present with a different expanded value. The first '<…>' is the variable name, the second is the earlier value and the third is the value that replaces it. The usual causes are a csolution variable whose name matches a built-in variable, or the same variable name set to different values in more than one of the scopes that apply to the context.

## Fix

Give each user variable a name that does not match a built-in variable, and define a variable with one value in only one scope (target build, build type or target type). If the same value is intended in several scopes, make the values identical. Check the variables of the build type and target type that apply to the context named in the message, and the variables under the target build. The later scope's value is the one used, so remove the duplicate you do not want.

## Trigger in the source

```cpp
if ((context.variables.find(key) != context.variables.end()) && (context.variables.at(key) != expandedValue)) {
```

## Note

The README does not document this message. The warning is only printed when the two values differ; identical redefinitions are silent. The built-in variable names come from RteConstants, which is not among the lines given, so the exact names that collide are not listed here. The 'from' value is the earlier value in context.variables, which may be a built-in value rather than a user value.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:238-242`
- `tools/projmgr/src/ProjMgrWorker.cpp:272-288`
- `tools/projmgr/src/ProjMgrWorker.cpp:283-284`
