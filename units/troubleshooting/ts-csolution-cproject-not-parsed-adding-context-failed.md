---
id: "ts-csolution-cproject-not-parsed-adding-context-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject not parsed, adding context failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject not parsed, adding context failed"]
symptom_regex: "^cproject not parsed, adding context failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:117"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`cproject not parsed, adding context failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (descriptor.west.app.empty() && descriptor.cmake.source.empty()) {
```
