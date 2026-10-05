---
id: "ts-csolution-no-target-set-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no target-set was found with filter"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no target-set was found with filter '<…>'"]
symptom_regex: "^no target\\-set was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:4869"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no target-set was found with filter '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (filteredTargetSets.empty()) {
```
