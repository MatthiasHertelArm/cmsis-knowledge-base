---
id: "ts-csolution-reading-gpdsc-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: reading gpdsc failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' generator '<…>' from component '<…>': reading gpdsc failed"]
symptom_regex: "^context '.+?' generator '.+?' from component '.+?': reading gpdsc failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2895"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`context '<…>' generator '<…>' from component '<…>': reading gpdsc failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!gpdscPack) {
```
