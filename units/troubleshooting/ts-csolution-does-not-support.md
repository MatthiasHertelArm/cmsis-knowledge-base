---
id: "ts-csolution-does-not-support"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: device '…' does not support '…: …'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["device '<…>' does not support '<…>: <…>'"]
symptom_regex: "^device '.+?' does not support '.+?: .+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1608"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The `processor:` node (in a target type or build type of the csolution.yml, or in the cproject.yml) asks for a feature the selected device or core does not have: an `endian:` the device does not use, `fpu: dp` on …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1536-1539", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1601-1637", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1711-1740"]
---

## Symptom

`device '<…>' does not support '<…>: <…>'`

## Cause

The `processor:` node (in a target type or build type of the csolution.yml, or in the cproject.yml) asks for a feature the selected device or core does not have: an `endian:` the device does not use, `fpu: dp` on a single-precision FPU, or `fpu`, `dsp`, `mve`, `trustzone` or `branch-protection` on a device without that feature. The `<…>` are the device and the `key: value` asked for.

## Fix

Remove the setting, or set it to `off` where the key allows it (e.g. `processor: trustzone: off`; `endian:` has no off), or select a device or processor that has the feature.

## Trigger in the source

```cpp
if ((endian != RteConstants::RTE_ENDIAN_CONFIGURABLE) &&
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1536-1539`
- `tools/projmgr/src/ProjMgrWorker.cpp:1601-1637`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1711-1740`
