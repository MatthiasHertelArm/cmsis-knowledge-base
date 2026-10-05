---
id: "ts-csolution-mlops-npu-macs-value-does-not-match-dfp-device-i"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops.npu.macs value does not match DFP device information"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["mlops.npu.macs value does not match DFP device information"]
symptom_regex: "^mlops\\.npu\\.macs value does not match DFP device information$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrMlops.cpp:292"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`mlops.npu.macs value does not match DFP device information`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (find_if(npuInfoItems.begin(), npuInfoItems.end(), matchesMacs) == npuInfoItems.end()) {
```
