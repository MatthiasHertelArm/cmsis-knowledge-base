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
summary: "A selected component is handled by a generator defined in its pack, and the generator's gpdsc file (its path prefixes the message) cannot be loaded: it does not exist yet because the generator has not been run for this …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2882-2898", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2049-2064", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:108-132", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteProject.cpp:1196-1214", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUtilsUnitTests.cpp:61-75", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestGenerator/RTE/Device/RteTestGen_ARMCM0/RteTest_Invalid.gpdsc"]
---

## Symptom

`context '<…>' generator '<…>' from component '<…>': reading gpdsc failed`

## Cause

A selected component is handled by a generator defined in its pack, and the generator's gpdsc file (its path prefixes the message) cannot be loaded: it does not exist yet because the generator has not been run for this context, or it is not valid XML/PDSC. The `<…>` are the context, the generator id and the component; RTE parser errors with details may follow.

## Fix

Run the generator for the context: `csolution run <name>.csolution.yml -g <generator-id> -c <context>` (`csolution list generators <name>.csolution.yml -c <context>` shows the ids). If the file exists, regenerate it or fix the XML error reported after this message.

## Trigger in the source

```cpp
if (!gpdscPack) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2882-2898`
- `tools/projmgr/src/ProjMgrWorker.cpp:2049-2064`
- `tools/projmgr/src/ProjMgrUtils.cpp:108-132`
- `libs/rtemodel/src/RteProject.cpp:1196-1214`
- `tools/projmgr/test/src/ProjMgrUtilsUnitTests.cpp:61-75`
- `tools/projmgr/test/data/TestGenerator/RTE/Device/RteTestGen_ARMCM0/RteTest_Invalid.gpdsc`
