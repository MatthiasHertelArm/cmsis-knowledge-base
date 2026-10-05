---
id: "ts-csolution-cproject-yml-files-should-be-placed-in-separate-"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject.yml files should be placed in separate sub-directories"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["cproject.yml files should be placed in separate sub-directories"]
symptom_regex: "^cproject\\.yml files should be placed in separate sub\\-directories$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:521"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`cproject.yml files should be placed in separate sub-directories`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (adjacent_find(dirs.begin(), dirs.end()) != dirs.end()) {
```
