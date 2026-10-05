---
id: "ts-csolution-pdsc-file-was-not-found-in"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: pdsc file was not found in"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["pdsc file was not found in: <…>"]
symptom_regex: "^pdsc file was not found in: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1807"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`pdsc file was not found in: <…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::Exists(pdscFile)) {
```
