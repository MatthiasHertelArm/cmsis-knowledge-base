---
id: "ts-csolution-does-not-match-any-device-pname"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: pname '…' does not match any device pname"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["pname '<…>' does not match any device pname"]
symptom_regex: "^pname '.+?' does not match any device pname$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:496"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `telnet:` entry under `target-set:` - `debugger:` in the csolution.yml has `pname:` set to a processor name the device does not have; `<…>` is that name."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:482", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:615", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestRunDebug/telnet.csolution.yml:86", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7369"]
---

## Symptom

`pname '<…>' does not match any device pname`

## Cause

A `telnet:` entry under `target-set:` - `debugger:` in the csolution.yml has `pname:` set to a processor name the device does not have; `<…>` is that name. The entry is ignored.

## Fix

Use one of the device's processor names (shown by `csolution list devices`, after the colon in `Device:Pname`) in `pname:`, or remove the entry.

## Trigger in the source

```cpp
if (pnames.find(pname) == pnames.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:482`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:615`
- `tools/projmgr/test/data/TestRunDebug/telnet.csolution.yml:86`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7369`
