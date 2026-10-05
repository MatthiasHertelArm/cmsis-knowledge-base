---
id: "ts-csolution-is-not-a-valid-command-see-csolution-help"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is not a valid command. See 'csolution --help'."
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["'<…>' is not a valid command. See 'csolution --help'."]
symptom_regex: "^'.+?' is not a valid command\\. See 'csolution \\-\\-help'\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:109"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'<…>' is not a valid command. See 'csolution --help'.`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (cmdOptionsDict.find(filter) == cmdOptionsDict.end()) {
```
