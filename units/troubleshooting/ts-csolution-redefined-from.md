---
id: "ts-csolution-redefined-from"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefined from"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["variable '<…>' redefined from '<…>' to '<…>'"]
symptom_regex: "^variable '.+?' redefined from '.+?' to '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:284"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`variable '<…>' redefined from '<…>' to '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if ((context.variables.find(key) != context.variables.end()) && (context.variables.at(key) != expandedValue)) {
```
