---
id: "ts-csolution-failed-to-read-latest-pack-information-from-pack"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: failed to read latest pack information from pack index"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["failed to read latest pack information from pack index"]
symptom_regex: "^failed to read latest pack information from pack index$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:6147"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`failed to read latest pack information from pack index`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_kernel->ReadPackLatestVerAndPath(latestPacks)) {
```
