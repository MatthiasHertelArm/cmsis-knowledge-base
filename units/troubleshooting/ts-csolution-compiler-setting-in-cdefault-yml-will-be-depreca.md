---
id: "ts-csolution-compiler-setting-in-cdefault-yml-will-be-depreca"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox "
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0"]
symptom_regex: "^'compiler' setting in cdefault\\.yml will be deprecated in CMSIS\\-Toolbox 3\\.0\\.0$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:45"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!cdefault.compiler.empty()) {
```
