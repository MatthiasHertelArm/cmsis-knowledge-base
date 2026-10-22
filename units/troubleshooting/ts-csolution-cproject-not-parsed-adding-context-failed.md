---
id: "ts-csolution-cproject-not-parsed-adding-context-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject not parsed, adding context failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject not parsed, adding context failed"]
symptom_regex: "^cproject not parsed, adding context failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:117"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Follow-up error: a project listed under projects: of the csolution.yml could not be loaded, because its cproject.yml was not found or failed YAML or schema parsing, so csolution cannot create its contexts."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:108-123", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:524-535", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:551-560"]
---

## Symptom

`cproject not parsed, adding context failed`

## Cause

Follow-up error: a project listed under projects: of the csolution.yml could not be loaded, because its cproject.yml was not found or failed YAML or schema parsing, so csolution cannot create its contexts. The message is prefixed with the cproject path.

## Fix

Fix the error reported before it for the same file (wrong `project:` path, YAML syntax or schema error), then run again.

## Trigger in the source

```cpp
if (descriptor.west.app.empty() && descriptor.cmake.source.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:108-123`
- `tools/projmgr/src/ProjMgr.cpp:524-535`
- `tools/projmgr/src/ProjMgr.cpp:551-560`
