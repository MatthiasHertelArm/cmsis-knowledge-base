---
id: "ts-csolution-more-than-one-valid-serialwire-element-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: more than one valid <serialwire> element found"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["more than one valid <serialwire> element found"]
symptom_regex: "^more than one valid <serialwire> element found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrRunDebug.cpp:605"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The device's effective trace properties contain more than one <serialwire> sink element without a Pname attribute."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:580-589", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:604-606"]
---

## Symptom

`more than one valid <serialwire> element found`

## Cause

The device's effective trace properties contain more than one <serialwire> sink element without a Pname attribute. The loop at lines 580-603 counts every such sink, and when the count is greater than one the tool warns, since only the first serial-wire sink is kept in the debug topology. The warning is about the device/pack description (PDSC device trace elements) rather than the csolution project file itself.

## Fix

Check the device or board PDSC trace definitions for the device, and keep a single <serialwire> element per processor (without a Pname attribute, since Pname-tagged traces are ignored). If several are declared for different processors, give them a Pname attribute so they are skipped here. If the pack is not yours, report the duplicate to the pack vendor.

## Trigger in the source

```cpp
if (serialWireCount > 1) {
```

## Note

The README does not document this message. The message is a warning, not an error, and the tool continues. The cause is inferred from the counting logic; which PDSC element produces the duplicate is not visible in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:580-589`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:604-606`
