---
id: "ts-csolution-file-is-missing-and-required-due-to-use-of-froze"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file is missing and required due to use of --frozen-packs option"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file is missing and required due to use of --frozen-packs option"]
symptom_regex: "^file is missing and required due to use of \\-\\-frozen\\-packs option$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:66"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`file is missing and required due to use of --frozen-packs option`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
} else if (frozenPacks) {
```
