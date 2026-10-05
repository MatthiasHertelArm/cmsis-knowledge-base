---
id: "ts-csolution-shall-contain-mapping-elements"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: shall contain mapping elements"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["node '<…>' shall contain mapping elements"]
symptom_regex: "^node '.+?' shall contain mapping elements$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:1753"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`node '<…>' shall contain mapping elements`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
} else if ((mappings.find(key) != mappings.end()) && (sequences.find(key) == sequences.end())) {
```
