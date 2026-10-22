---
id: "ts-csolution-is-not-selectable-as-active-target-set"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' is not selectable as active target-set"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["'<…>' is not selectable as active target-set"]
symptom_regex: "^'.+?' is not selectable as active target\\-set$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:6321"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The value given for the active target (the --active option, as <target-type>@<target-set>) does not match anything declared in the csolution's target-types."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6299-6300", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6302-6317", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6320-6321"]
---

## Symptom

`'<…>' is not selectable as active target-set`

## Cause

The value given for the active target (the --active option, as <target-type>@<target-set>) does not match anything declared in the csolution's target-types. PopulateActiveTargetSet splits the string at '@' and looks for a target-type with that name. If none matches, the active target-type stays empty. If the target-type matches but no target-set with the given name exists under it, the lookup also fails. Either way the message prints the whole string the user passed.

## Fix

Use an active target that exists in the csolution file: a target-type name from target-types, optionally followed by @ and a target-set name listed under that target-type. Check the spelling of both parts against target-types in the csolution YAML. Dropping the @ part selects the target-type alone, provided it is declared.

## Trigger in the source

```cpp
if (m_activeTargetType.empty() || (!targetSetFound && !targetSet.empty())) {
```

## Note

The message is not documented in the README. The empty-string case (--active with no value) takes the first target-type and does not reach this error.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6299-6300`
- `tools/projmgr/src/ProjMgrWorker.cpp:6302-6317`
- `tools/projmgr/src/ProjMgrWorker.cpp:6320-6321`
