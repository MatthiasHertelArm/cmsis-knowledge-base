---
id: "ts-csolution-failed-to-load-and-insert-packs"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: failed to load and insert packs"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["failed to load and insert packs"]
symptom_regex: "^failed to load and insert packs$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:575"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`failed to load and insert packs`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_kernel->LoadAndInsertPacks(m_loadedPacks, pdscFiles)) {
```
