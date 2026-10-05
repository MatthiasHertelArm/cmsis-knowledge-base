---
id: "ts-csolution-no-default-unnamed-target-set-for"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no default unnamed target set for"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: <…>no default unnamed target set for '<…>'<…>target set '<…>' not found<…>"]
symptom_regex: "^mlops: .+?no default unnamed target set for '.+?'.+?target set '.+?' not found.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrMlops.cpp:85"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`mlops: <…>no default unnamed target set for '<…>'<…>target set '<…>' not found<…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!GetTargetSetItemRef(targetType, targetSetName, simulatorDefault, targetSetItem)) {
```
