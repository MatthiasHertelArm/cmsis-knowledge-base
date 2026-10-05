---
id: "ts-csolution-customization-of-intermediate-directory-intdir-i"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: customization of intermediate directory 'intdir' is ignored by the cbu"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend"]
symptom_regex: "^customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:204"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_cbuild2cmake) {
```
