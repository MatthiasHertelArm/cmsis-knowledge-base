---
id: "ts-csolution-does-not-support"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: does not support"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["device '<…>' does not support '<…>: <…>'"]
symptom_regex: "^device '.+?' does not support '.+?: .+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1608"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`device '<…>' does not support '<…>: <…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if ((endian != RteConstants::RTE_ENDIAN_CONFIGURABLE) &&
```
