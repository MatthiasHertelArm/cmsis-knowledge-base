---
id: "ts-csolution-reading-gpdsc-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' generator '…' from component '…': reading gpdsc failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' generator '<…>' from component '<…>': reading gpdsc failed"]
symptom_regex: "^context '.+?' generator '.+?' from component '.+?': reading gpdsc failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2895"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProcessGpdsc calls ProjMgrUtils::ReadGpdscFile for each generator gpdsc file that a context uses."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2892", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2894-2898", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2900-2902"]
---

## Symptom

`context '<…>' generator '<…>' from component '<…>': reading gpdsc failed`

## Cause

ProcessGpdsc calls ProjMgrUtils::ReadGpdscFile for each generator gpdsc file that a context uses. When that call returns no package, the tool cannot load the gpdsc file named in the message, so it logs this error and stops processing the context. The quoted context name, generator and component come from the context's gpdsc entry, and the gpdsc file path is passed as the logger's file argument. The source lines shown do not reveal which read step fails, so the exact reason (missing file, unreadable file or malformed content) is not confirmed here. A file that is readable but fails validation only produces the separate 'gpdsc validation failed' warning, not this error.

## Fix

Open the gpdsc file named in the message and check that it exists at that path, is readable, and is well-formed XML that the generator pack provides. If the file is missing, correct the component or pack setup that refers to the generator so that the pack containing the gpdsc is installed. Then rerun the csolution command. The source lines do not show a further workaround.

## Trigger in the source

```cpp
if (!gpdscPack) {
```

## Note

The message is not documented in the README. The trigger is a null return from ProjMgrUtils::ReadGpdscFile, and its implementation is not in the lines given, so the file-level causes listed are a reading, not confirmed behaviour.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2892`
- `tools/projmgr/src/ProjMgrWorker.cpp:2894-2898`
- `tools/projmgr/src/ProjMgrWorker.cpp:2900-2902`
