---
id: "ts-csolution-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["pack path: <…> does not exist"]
symptom_regex: "^pack path: .+? does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1800"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`pack path: <…> does not exist`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::Exists(package.path)) {
```
