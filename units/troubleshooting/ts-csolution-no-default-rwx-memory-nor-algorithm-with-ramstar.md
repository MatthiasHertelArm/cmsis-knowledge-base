---
id: "ts-csolution-no-default-rwx-memory-nor-algorithm-with-ramstar"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no default rwx memory nor algorithm with ramstart/size was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no default rwx memory nor algorithm with ramstart/size was found"]
symptom_regex: "^no default rwx memory nor algorithm with ramstart/size was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrRunDebug.cpp:391"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no default rwx memory nor algorithm with ramstart/size was found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (defaultRam.size != 0) {
```
