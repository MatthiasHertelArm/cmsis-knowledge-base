---
id: "ts-csolution-shall-contain-sequence-elements"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: shall contain sequence elements"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["node '<…>' shall contain sequence elements"]
symptom_regex: "^node '.+?' shall contain sequence elements$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:1745"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`node '<…>' shall contain sequence elements`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
} else if ((sequences.find(key) != sequences.end()) && (mappings.find(key) == mappings.end())) {
```
