---
id: "ts-csolution-redefinition-from"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefinition from '…' into '…' is not allowed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["redefinition from '<…>' into '<…>' is not allowed"]
symptom_regex: "^redefinition from '.+?' into '.+?' is not allowed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:797"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "GetPrecedentValue keeps the first non-empty value it receives in outValue and rejects a later, different non-empty value."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:794-803", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:796-797"]
---

## Symptom

`redefinition from '<…>' into '<…>' is not allowed`

## Cause

GetPrecedentValue keeps the first non-empty value it receives in outValue and rejects a later, different non-empty value. The message prints the earlier value as '<…>' (from) and the new conflicting value as '<…>' (into). So the same setting, such as a device, board or other project-level item, is given two different values by different sources that feed the same outValue. The callers are not in the lines given, so the exact sources cannot be confirmed from this excerpt.

## Fix

Find the two places that set the value named in the message, using the 'from' and 'into' strings as the two values, and make them agree or remove one of them. Check the csolution project YAML and any build-type or target overrides for that value. Then rerun csolution.

## Trigger in the source

```cpp
if (!outValue.empty() && (outValue != element)) {
```

## Note

The message names no setting, so which item is conflicting is not visible from the source lines given; the callers of GetPrecedentValue would confirm which setting it is. The README has no entry for this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:794-803`
- `tools/projmgr/src/ProjMgrWorker.cpp:796-797`
