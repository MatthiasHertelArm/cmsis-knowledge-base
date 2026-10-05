---
id: "ts-csolution-is-deprecated-at-this-level-and-accepted-in-csol"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is deprecated at this level and accepted in *.csolution.yml only"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["<…>'device: Dname'<…>'board:' node<…> is deprecated at this level and accepted in *.csolution.yml only"]
symptom_regex: "^.+?'device: Dname'.+?'board:' node.+? is deprecated at this level and accepted in \\*\\.csolution\\.yml only$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:1127"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`<…>'device: Dname'<…>'board:' node<…> is deprecated at this level and accepted in *.csolution.yml only`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if ((key == YAML_DEVICE) && regex_match(value, regex("^:[ -9;-~]+$"))) {
```
