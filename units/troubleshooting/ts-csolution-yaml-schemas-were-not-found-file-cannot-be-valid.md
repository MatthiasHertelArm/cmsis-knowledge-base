---
id: "ts-csolution-yaml-schemas-were-not-found-file-cannot-be-valid"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: yaml schemas were not found, file cannot be validated"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["yaml schemas were not found, file cannot be validated"]
symptom_regex: "^yaml schemas were not found, file cannot be validated$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:28"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`yaml schemas were not found, file cannot be validated`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if(schemaFile.empty()) {
```
