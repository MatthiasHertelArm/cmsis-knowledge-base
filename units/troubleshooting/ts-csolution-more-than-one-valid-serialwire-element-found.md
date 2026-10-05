---
id: "ts-csolution-more-than-one-valid-serialwire-element-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: more than one valid <serialwire> element found"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["more than one valid <serialwire> element found"]
symptom_regex: "^more than one valid <serialwire> element found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrRunDebug.cpp:605"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`more than one valid <serialwire> element found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (serialWireCount > 1) {
```
