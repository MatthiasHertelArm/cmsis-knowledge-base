---
id: "ts-csolution-contains-more-than-one"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: contains more than one"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' contains more than one '<…> file, PLM may fail"]
symptom_regex: "^'.+?' contains more than one '.+? file, PLM may fail$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrCbuild.cpp:252"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'<…>' contains more than one '<…> file, PLM may fail`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (backupFiles.size() > 1) {
```
