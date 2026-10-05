---
id: "ts-csolution-contains-non-portable-backslash-use-forward-slas"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: contains non-portable backslash, use forward slash instead"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' contains non-portable backslash, use forward slash instead"]
symptom_regex: "^'.+?' contains non\\-portable backslash, use forward slash instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:335"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'<…>' contains non-portable backslash, use forward slash instead`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (value.find('\\') != string::npos) {
```
