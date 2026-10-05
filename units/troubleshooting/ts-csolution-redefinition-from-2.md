---
id: "ts-csolution-redefinition-from-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefinition from"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["redefinition from '<…>' into '<…>'"]
symptom_regex: "^redefinition from '.+?' into '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3005"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`redefinition from '<…>' into '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (acceptRedefinition) {
```
