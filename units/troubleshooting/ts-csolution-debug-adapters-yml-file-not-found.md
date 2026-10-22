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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:939"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "RunListDebuggers gets the debug-adapters file path from GetDebugAdaptersFile() and stops with this error when that path is empty."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:937-941"]
---

## Symptom

`debug-adapters.yml file not found`

## Cause

RunListDebuggers gets the debug-adapters file path from GetDebugAdaptersFile() and stops with this error when that path is empty. The lines given do not show how GetDebugAdaptersFile() searches for the file, so the reason it comes back empty (no file in the expected location, or a missing installation component) is not visible here.

## Fix

The lines given do not show where the tool looks for debug-adapters.yml. Check that the CMSIS toolbox installation the csolution command comes from includes this file, and that it is not missing or moved. Then run the listing command again. Beyond that, the lines given offer no further fix.

## Trigger in the source

```cpp
if (debugAdapters.empty()) {
```

## Note

The message has no code and the README does not document it. The trigger is a plain empty-path check, but GetDebugAdaptersFile() is not among the lines provided, so the search location and the user-facing cause are inferred.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:937-941`
