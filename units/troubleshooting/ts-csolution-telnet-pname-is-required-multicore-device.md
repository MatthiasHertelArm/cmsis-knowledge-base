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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrRunDebug.cpp:492"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The device has more than one processor, and an entry under `debugger: telnet:` (target-set in the csolution.yml) has no `pname:`. csolution cannot tell which core the telnet settings belong to and skips the entry."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:482-494", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:2406-2420", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7366-7376"]
---

## Symptom

`'telnet:' pname is required (multicore device)`

## Cause

The device has more than one processor, and an entry under `debugger: telnet:` (target-set in the csolution.yml) has no `pname:`. csolution cannot tell which core the telnet settings belong to and skips the entry.

## Fix

Add the processor name to each telnet entry, e.g. `telnet: - mode: monitor  pname: cm0_core0  port: 4444`. The pnames are those of the device's processors (the `:<pname>` used in `device:`).

## Trigger in the source

```cpp
if (pnames.size() > 1 && value.pname.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:482-494`
- `tools/projmgr/schemas/common.schema.json:2406-2420`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7366-7376`
