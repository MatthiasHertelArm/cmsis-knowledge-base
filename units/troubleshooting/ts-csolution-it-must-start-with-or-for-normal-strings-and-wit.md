---
id: "ts-csolution-it-must-start-with-or-for-normal-strings-and-wit"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: it must start with '.' or '+' for normal strings and with '^' or '\\' f"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["type '<…>': it must start with '.' or '+' for normal strings and with '^' or '\\' for regex patterns"]
symptom_regex: "^type '.+?': it must start with '\\.' or '\\+' for normal strings and with '\\^' or '\\\\' for regex patterns$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:712"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`type '<…>': it must start with '.' or '+' for normal strings and with '^' or '\' for regex patterns`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (((buildDelimiter > 0) && (targetDelimiter > 0) && (regexDelimiter > 0))) {
```
