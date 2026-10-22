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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrRunDebug.cpp:391"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "CheckDefaultRam is called with a default RAM descriptor whose size is zero, meaning the tool found no RAM region for the debug target."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:387-393"]
---

## Symptom

`no default rwx memory nor algorithm with ramstart/size was found`

## Cause

CheckDefaultRam is called with a default RAM descriptor whose size is zero, meaning the tool found no RAM region for the debug target. The message names the two places it looks: a memory with rwx access in the device description, or a flash programming algorithm that defines ramstart and size. The source lines given do not show how defaultRam is filled, so the exact input that leaves it empty is inferred from the trigger, not confirmed.

## Fix

Check the device or board pack that the csolution project uses. Confirm that its PDSC describes a memory with rwx access, or a flash algorithm with ramstart and ramsize, that covers the RAM the debugger should use. If the pack has none, the device data is incomplete and needs a pack that defines it, or a corrected device selection in the csolution project. The source lines given do not show a further setting to change.

## Trigger in the source

```cpp
if (defaultRam.size != 0) {
```

## Note

The README does not document this message. The trigger and the error text are clear in the source, but the path from PDSC or SVD input to the RamType size is outside the lines given, so the cause of the zero size is inferred.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:387-393`
