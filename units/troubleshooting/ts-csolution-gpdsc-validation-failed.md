---
id: "ts-csolution-gpdsc-validation-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' generator '…' from component '…': gpdsc validation failed"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["context '<…>' generator '<…>' from component '<…>': gpdsc validation failed"]
symptom_regex: "^context '.+?' generator '.+?' from component '.+?': gpdsc validation failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2901"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2891-2905", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:108-132", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUtilsUnitTests.cpp:49-59", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestGenerator/RTE/Device/RteTestGen_ARMCM0/RteTest_Warning.gpdsc:28"]
---

## Symptom

`context '<…>' generator '<…>' from component '<…>': gpdsc validation failed`

## Cause

The gpdsc file that a pack generator wrote for a component (its path prefixes the message) loads, but fails pack validation without a specific error, e.g. a component in it references a condition that does not exist. csolution still uses the file. The `<…>` are the context, the generator id and the component that started the generator.

## Fix

Re-run the generator so it writes a fresh gpdsc: `csolution run <name>.csolution.yml -g <generator-id> -c <context>`. If the warning stays, the generator or its pack produces an inconsistent gpdsc; update them or report it to their vendor.

## Trigger in the source

```cpp
if (!validGpdsc) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2891-2905`
- `tools/projmgr/src/ProjMgrUtils.cpp:108-132`
- `tools/projmgr/test/src/ProjMgrUtilsUnitTests.cpp:49-59`
- `tools/projmgr/test/data/TestGenerator/RTE/Device/RteTestGen_ARMCM0/RteTest_Warning.gpdsc:28`
