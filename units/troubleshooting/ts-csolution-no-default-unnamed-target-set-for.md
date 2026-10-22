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
summary: "`mlops:` - `hardware:` or `simulator:` - `target:` names a target type whose target sets do not contain the requested one."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:35", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:84", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1176", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7990"]
---

## Symptom

`mlops: <…>no default unnamed target set for '<…>'<…>target set '<…>' not found<…>`

## Cause

`mlops:` - `hardware:` or `simulator:` - `target:` names a target type whose target sets do not contain the requested one. Without `@<set>` (e.g. `target: Hardware`) csolution needs a `target-set:` entry with an empty `set:` name and reports `no default unnamed target set for '<type>'`; with `target: <type>@<set>` it reports `target set '<type>@<set>' not found` when no entry has that `set:` name.

## Fix

Name an existing set in `target: <type>@<set>`, or add the set under the target type in the csolution.yml: `target-set:` - `set: <set>` (an entry with an empty `set:` serves as the default).

## Trigger in the source

```cpp
if (!GetTargetSetItemRef(targetType, targetSetName, simulatorDefault, targetSetItem)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:35`
- `tools/projmgr/src/ProjMgrMlops.cpp:84`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1176`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7990`
