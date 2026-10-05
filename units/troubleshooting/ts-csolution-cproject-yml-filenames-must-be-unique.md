---
id: "ts-csolution-cproject-yml-filenames-must-be-unique"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject.yml filenames must be unique"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject.yml filenames must be unique"]
symptom_regex: "^cproject\\.yml filenames must be unique$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:517"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`cproject.yml filenames must be unique`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (adjacent_find(names.begin(), names.end()) != names.end()) {
```
