---
id: "ts-csolution-debug-adapters-yml-file-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: debug-adapters.yml file not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["debug-adapters.yml file not found"]
symptom_regex: "^debug\\-adapters\\.yml file not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:939"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list debuggers` reads etc/debug-adapters.yml of the CMSIS-Toolbox installation (the etc folder next to the bin folder that contains csolution), and that file is missing, e.g. a csolution binary copied out of its installation or an incomplete installation."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:935-941", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1276-1284", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7738-7743"]
---

## Symptom

`debug-adapters.yml file not found`

## Cause

`csolution list debuggers` reads etc/debug-adapters.yml of the CMSIS-Toolbox installation (the etc folder next to the bin folder that contains csolution), and that file is missing, e.g. a csolution binary copied out of its installation or an incomplete installation.

## Fix

Run csolution from a complete CMSIS-Toolbox installation with bin/ and etc/ side by side, or reinstall CMSIS-Toolbox.

## Trigger in the source

```cpp
if (debugAdapters.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:935-941`
- `tools/projmgr/src/ProjMgr.cpp:1276-1284`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7738-7743`
