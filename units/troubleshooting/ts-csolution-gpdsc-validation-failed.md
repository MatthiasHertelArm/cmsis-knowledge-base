---
id: "ts-csolution-gpdsc-validation-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: gpdsc validation failed"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["context '<…>' generator '<…>' from component '<…>': gpdsc validation failed"]
symptom_regex: "^context '.+?' generator '.+?' from component '.+?': gpdsc validation failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2901"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`context '<…>' generator '<…>' from component '<…>': gpdsc validation failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!validGpdsc) {
```
