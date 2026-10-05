---
id: "ts-csolution-does-not-exist-or-is-not-selected"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: does not exist or is not selected"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' referenced by access sequence '<…>' does not exist or is not selected"]
symptom_regex: "^context '.+?' referenced by access sequence '.+?' does not exist or is not selected$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3777"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`context '<…>' referenced by access sequence '<…>' does not exist or is not selected`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (genDep && refContext.name != context.name) {
```
