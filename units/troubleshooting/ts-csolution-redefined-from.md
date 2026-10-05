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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:284"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:272", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:238", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestLayers/variables-redefinition.csolution.yml:5", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2498"]
---

## Symptom

`variable '<…>' redefined from '<…>' to '<…>'`

## Cause

The same variable is set to different values under `variables:` at more than one level of the csolution.yml, at solution level, in a build type and in a target type; the placeholders are the name, the earlier and the later value. They are applied in that order and the later value wins, so the target-type value takes precedence. A user variable that reuses a built-in name such as `Project` or `BuildType` also triggers it.

## Fix

Define the variable at one level only, or give it the same value everywhere; rename variables that clash with built-in names.

## Trigger in the source

```cpp
if ((context.variables.find(key) != context.variables.end()) && (context.variables.at(key) != expandedValue)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:272`
- `tools/projmgr/src/ProjMgrWorker.cpp:238`
- `tools/projmgr/test/data/TestLayers/variables-redefinition.csolution.yml:5`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2498`
