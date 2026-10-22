---
id: "ts-csolution-no-default-unnamed-target-set-for"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops: …no default unnamed target set for '…'…target set '…' not found…"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: <…>no default unnamed target set for '<…>'<…>target set '<…>' not found<…>"]
symptom_regex: "^mlops: .+?no default unnamed target set for '.+?'.+?target set '.+?' not found.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrMlops.cpp:85"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The mlops section of the csolution YAML names a target type (the mlops target string is 'type' or 'type@set') for which no target set can be picked."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:35-57", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:82-89"]
---

## Symptom

`mlops: <…>no default unnamed target set for '<…>'<…>target set '<…>' not found<…>`

## Cause

The mlops section of the csolution YAML names a target type (the mlops target string is 'type' or 'type@set') for which no target set can be picked. When the target set part is empty, the tool looks for a default unnamed target set: a target set whose debugger is Arm-FVP when the simulator default is used, or any non-Arm-FVP one for hardware. The message's '<target type>' is the type named in the mlops entry, and it appears because the type exists but none of its target sets matches that default rule.

## Fix

Check the target-type definition in the csolution YAML for the named target type and make sure it has a target set matching the default (an Arm-FVP debugger for simulation, a non-FVP debugger for hardware). Alternatively, name the target set explicitly in the mlops target as 'type@set' using a set name that exists in that target type.

## Trigger in the source

```cpp
if (!GetTargetSetItemRef(targetType, targetSetName, simulatorDefault, targetSetItem)) {
```

## Note

The message text uses the target type for the '<…>' slot in the unnamed case, so the wording 'for <type>' refers to the target type, not a set name. The lookup that fails here is GetTargetSetItemRef called with no set name, and the rule it applies (Arm-FVP debugger versus other) is read from the source. The README does not document this message; the cause and fix are my reading of the source and the exact user-facing wording may need checking against a real build.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:35-57`
- `tools/projmgr/src/ProjMgrMlops.cpp:82-89`
