---
id: "ts-csolution-invalid-pattern"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: invalid pattern"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid pattern '<…>': <…>"]
symptom_regex: "^invalid pattern '.+?': .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:719"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`invalid pattern '<…>': <…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (regexDelimiter == 0) {
```
