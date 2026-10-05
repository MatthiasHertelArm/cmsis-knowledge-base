---
id: "ts-csolution-access-sequence-pack-was-not-loaded-pack"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: access sequence pack was not loaded: '$Pack("
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["access sequence pack was not loaded: '$Pack(<…>)$'"]
symptom_regex: "^access sequence pack was not loaded: '\\$Pack\\(.+?\\)\\$'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3703"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`access sequence pack was not loaded: '$Pack(<…>)$'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (replacement.empty()) {
```
