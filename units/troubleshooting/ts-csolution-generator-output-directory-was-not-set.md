---
id: "ts-csolution-generator-output-directory-was-not-set"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator output directory was not set"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator output directory was not set"]
symptom_regex: "^generator output directory was not set$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5697"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator output directory was not set`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (options.path.empty()) {
```
