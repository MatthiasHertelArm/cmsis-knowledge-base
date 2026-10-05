---
id: "ts-csolution-ignoring-conflict-component"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: ignoring conflict: component"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["ignoring conflict: component '<…>' is listed multiple times"]
symptom_regex: "^ignoring conflict: component '.+?' is listed multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3906"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`ignoring conflict: component '<…>' is listed multiple times`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (ignoreDuplicates) {
```
