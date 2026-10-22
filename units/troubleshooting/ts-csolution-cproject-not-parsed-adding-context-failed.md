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
summary: "AddContexts is called for a cproject file path that is not in the parser's parsed cprojects map, and the call carries no west app and no cmake source in its descriptor, so there is no fallback project id to …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:113-118", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:120-121"]
---

## Symptom

`cproject not parsed, adding context failed`

## Cause

AddContexts is called for a cproject file path that is not in the parser's parsed cprojects map, and the call carries no west app and no cmake source in its descriptor, so there is no fallback project id to create the context from. The cproject file named in the message (the cprojectFile argument) was therefore never read or parsed, most likely because it is missing from the csolution, misspelled, or was not loaded before the context was requested.

## Fix

Check that the .cproject file path the message shows exists and is listed in the csolution's projects section with the correct relative path, then fix any spelling or location mismatch and run the command again. The source does not show a further workaround beyond making the cproject parse successfully.

## Trigger in the source

```cpp
if (descriptor.west.app.empty() && descriptor.cmake.source.empty()) {
```

## Note

The message is printed by ProjMgrLogger::Get().Error, and the cproject path is passed as the third argument, so it appears after the text. The exact reason the file was not parsed is not visible in these lines; the cause above is an inference from the lookup and the branch. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:113-118`
- `tools/projmgr/src/ProjMgrWorker.cpp:120-121`
