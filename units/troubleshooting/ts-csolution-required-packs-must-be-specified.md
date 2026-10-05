---
id: "ts-csolution-required-packs-must-be-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: required packs must be specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["required packs must be specified"]
symptom_regex: "^required packs must be specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:563"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`required packs must be specified`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (noPackRequirements && (m_loadPacksPolicy == LoadPacksPolicy::REQUIRED)) {
```
