---
id: "ts-csolution-does-not-accept-more-than"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: does not accept more than"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["component '<…>' does not accept more than <…> instance(s)"]
symptom_regex: "^component '.+?' does not accept more than .+? instance\\(s\\)$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2042"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`component '<…>' does not accept more than <…> instance(s)`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (item.instances > matchedComponentInstance->GetMaxInstances()) {
```
