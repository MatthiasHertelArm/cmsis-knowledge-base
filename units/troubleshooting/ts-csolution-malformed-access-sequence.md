---
id: "ts-csolution-malformed-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: malformed access sequence"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["malformed access sequence: '<…>"]
symptom_regex: "^malformed access sequence: '.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3722"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`malformed access sequence: '<…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteUtils::GetAccessSequence(offset, input, sequence, '$', '$')) {
```
