---
id: "ts-csolution-must-have-the-format-pack-vendor-name"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: )' must have the format '$Pack(vendor::name)$"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["access sequence '$Pack(<…>)' must have the format '$Pack(vendor::name)$'"]
symptom_regex: "^access sequence '\\$Pack\\(.+?\\)' must have the format '\\$Pack\\(vendor::name\\)\\$'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3688"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`access sequence '$Pack(<…>)' must have the format '$Pack(vendor::name)$'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (packInfo.vendor.empty() || packInfo.name.empty()) {
```
