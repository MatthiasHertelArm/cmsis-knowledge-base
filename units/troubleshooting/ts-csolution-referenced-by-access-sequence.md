---
id: "ts-csolution-referenced-by-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: referenced by access sequence"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' referenced by access sequence '<…>' is not compatible"]
symptom_regex: "^context '.+?' referenced by access sequence '.+?' is not compatible$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3746"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`context '<…>' referenced by access sequence '<…>' is not compatible`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (compatibleContexts.empty()) {
```
