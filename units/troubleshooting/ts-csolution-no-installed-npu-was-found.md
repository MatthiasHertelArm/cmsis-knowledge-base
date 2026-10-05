---
id: "ts-csolution-no-installed-npu-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed NPU was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed NPU was found"]
symptom_regex: "^no installed NPU was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:4386"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no installed NPU was found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (npuInfos.empty()) {
```
