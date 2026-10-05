---
id: "ts-csolution-no-packs-were-found-for-version-check-with-filte"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no packs were found for version check with filter"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no packs were found for version check with filter '<…>'"]
symptom_regex: "^no packs were found for version check with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:6209"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no packs were found for version check with filter '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (matchedPacks.empty()) {
```
