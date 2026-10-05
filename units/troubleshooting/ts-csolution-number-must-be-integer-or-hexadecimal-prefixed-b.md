---
id: "ts-csolution-number-must-be-integer-or-hexadecimal-prefixed-b"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: number must be integer or hexadecimal prefixed by 0x"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["number must be integer or hexadecimal prefixed by 0x"]
symptom_regex: "^number must be integer or hexadecimal prefixed by 0x$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:392"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`number must be integer or hexadecimal prefixed by 0x`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!regex_match(value, regex("^(0x[0-9a-fA-F]+)$|^([0-9]*)$"))) {
```
