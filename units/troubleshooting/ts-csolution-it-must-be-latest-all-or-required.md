---
id: "ts-csolution-it-must-be-latest-all-or-required"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: unknown load option: '…', it must be 'latest', 'all' or 'required'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["unknown load option: '<…>', it must be 'latest', 'all' or 'required'"]
symptom_regex: "^unknown load option: '.+?', it must be 'latest', 'all' or 'required'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:478"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The `-l`/`--load` option was given a value other than `latest`, `all` or `required`; `<…>` is that value."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:468", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:298", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3990"]
---

## Symptom

`unknown load option: '<…>', it must be 'latest', 'all' or 'required'`

## Cause

The `-l`/`--load` option was given a value other than `latest`, `all` or `required`; `<…>` is that value.

## Fix

Use one of the three values, e.g. `-l latest`, or leave the option out to use the default pack loading.

## Trigger in the source

```cpp
} else if (m_loadPacksPolicy == "required") {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:468`
- `tools/projmgr/src/ProjMgr.cpp:298`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3990`
