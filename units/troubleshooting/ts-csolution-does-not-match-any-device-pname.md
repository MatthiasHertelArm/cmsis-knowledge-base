---
id: "ts-csolution-does-not-match-any-device-pname"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: does not match any device pname"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["pname '<…>' does not match any device pname"]
symptom_regex: "^pname '.+?' does not match any device pname$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrRunDebug.cpp:496"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`pname '<…>' does not match any device pname`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (pnames.find(pname) == pnames.end()) {
```
