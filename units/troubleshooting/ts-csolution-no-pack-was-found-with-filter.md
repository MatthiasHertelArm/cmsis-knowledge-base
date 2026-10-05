---
id: "ts-csolution-no-pack-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no pack was found with filter"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no pack was found with filter '<…>'"]
symptom_regex: "^no pack was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:4267"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no pack was found with filter '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (filteredPacks.empty()) {
```
