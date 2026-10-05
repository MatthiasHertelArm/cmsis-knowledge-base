---
id: "ts-csolution-uses-unknown-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: uses unknown generator"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["<…>Component <…> uses unknown generator <…>"]
symptom_regex: "^.+?Component .+? uses unknown generator .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrCbuild.cpp:179"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`<…>Component <…> uses unknown generator <…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
} else if (contains_key(context->extGen, component.generator)) {
```
