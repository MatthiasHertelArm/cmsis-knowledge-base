---
id: "ts-csolution-was-not-recognized"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: was not recognized"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["key '<…>' was not recognized"]
symptom_regex: "^key '.+?' was not recognized$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:1738"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`key '<…>' was not recognized`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (keys.find(item.first.as<string>()) == keys.end()) {
```
