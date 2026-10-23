---
id: "ts-csolution-no-default-rwx-memory-nor-algorithm-with-ramstar"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no default rwx memory nor algorithm with ramstart/size was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no default rwx memory nor algorithm with ramstart/size was found"]
symptom_regex: "^no default rwx memory nor algorithm with ramstart/size was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrRunDebug.cpp:391"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "While writing the run and debug information (cbuild-run.yml), csolution needs a RAM area to run a flash programming algorithm that has no RAM address of its own: a default DFP/BSP algorithm without RAMstart/RAMsize, or a `memory:` entry of the …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:387", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:137", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:240", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:2134", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:178"]
---

## Symptom

`no default rwx memory nor algorithm with ramstart/size was found`

## Cause

While writing the run and debug information (cbuild-run.yml), csolution needs a RAM area to run a flash programming algorithm that has no RAM address of its own: a default DFP/BSP algorithm without RAMstart/RAMsize, or a `memory:` entry of the target type with `algorithm:` but without `ram-start:`/`ram-size:`. It falls back to the first default memory with `rwx` access or the first algorithm with RAMstart/RAMsize in the DFP or BSP, and found neither.

## Fix

For your own algorithm add the RAM to the `memory:` entry under `target-types:` in the csolution.yml, e.g. `ram-start: 0x20000000` and `ram-size: 0x10000`. If the algorithm comes from the DFP or BSP, report the missing RAM information to the pack vendor.

## Trigger in the source

```cpp
if (defaultRam.size != 0) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:387`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:137`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:240`
- `tools/projmgr/schemas/common.schema.json:2134`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:178`
