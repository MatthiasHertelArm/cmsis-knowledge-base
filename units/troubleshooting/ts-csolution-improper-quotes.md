---
id: "ts-csolution-improper-quotes"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: , improper quotes"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid define: <…>, improper quotes"]
symptom_regex: "^invalid define: .+?, improper quotes$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:450"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`invalid define: <…>, improper quotes`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!isValid) {
```
