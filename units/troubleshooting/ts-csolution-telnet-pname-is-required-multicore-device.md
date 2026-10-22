---
id: "ts-csolution-telnet-pname-is-required-multicore-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: 'telnet:' pname is required (multicore device)"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'telnet:' pname is required (multicore device)"]
symptom_regex: "^'telnet:' pname is required \\(multicore device\\)$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrRunDebug.cpp:492"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The project's device has more than one processor (pnames has more than one entry, i.e. a multicore device), and a 'telnet:' entry in the csolution debugger settings has no pname."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:490-494", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:482-483"]
---

## Symptom

`'telnet:' pname is required (multicore device)`

## Cause

The project's device has more than one processor (pnames has more than one entry, i.e. a multicore device), and a 'telnet:' entry in the csolution debugger settings has no pname. CollectTelnetOptions only accepts telnet entries that name a processor on a multicore device; an entry with an empty pname is skipped and not applied to any core.

## Fix

Give each telnet entry a pname that matches a processor of the device, for example under debugger: telnet: with a key naming the processor (the key is the pname used in the device description), and set its mode or port there. Then rerun the build or debug command so the setting is applied to that core.

## Trigger in the source

```cpp
if (pnames.size() > 1 && value.pname.empty()) {
```

## Note

The source shows the entry is skipped with this warning; the exact YAML key layout for naming the pname is inferred from the loop over context.debugger.telnet keyed by pname, not from documentation. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:490-494`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:482-483`
