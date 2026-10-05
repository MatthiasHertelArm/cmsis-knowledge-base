---
id: "ts-csolution-no-packs-were-found-for-version-check"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no packs were found for version check"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no packs were found for version check"]
symptom_regex: "^no packs were found for version check$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:6202"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no packs were found for version check`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (checkPackResults.empty()) {
```
