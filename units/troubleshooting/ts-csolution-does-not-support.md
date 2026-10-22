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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1608"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The user's csolution YAML sets an endian value (the `endian` key of the processor or device selection) for a device whose pack fixes its endianness to a different value."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1603-1607", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1608-1609"]
---

## Symptom

`device '<…>' does not support '<…>: <…>'`

## Cause

The user's csolution YAML sets an endian value (the `endian` key of the processor or device selection) for a device whose pack fixes its endianness to a different value. At ProjMgrWorker.cpp:1603-1607 the tool reads the device's target attribute for RTE_DENDIAN, and if it is not the configurable value and differs from the value the user requested, it prints this warning. The `<…>` device is the device name from the context, and the `endian: <…>` part is the user's requested value.

## Fix

Remove the `endian` setting from the csolution YAML so the device default applies, or set it to the endianness the device supports. If the project needs the requested endianness, select a device or variant whose pack declares that endianness.

## Trigger in the source

```cpp
if ((endian != RteConstants::RTE_ENDIAN_CONFIGURABLE) &&
```

## Note

The message is a warning, not an error, so the build continues with the device's fixed endianness. The printed text does not name the device's supported value. The same message format is also used for fpu, dsp, mve, trustzone and branch-protection checks at lines 1617 and 1632-1633, so the text alone does not identify which attribute failed beyond the key shown. The id has no code in the message header.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1603-1607`
- `tools/projmgr/src/ProjMgrWorker.cpp:1608-1609`
