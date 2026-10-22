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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrRunDebug.cpp:496"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution YAML has a `debugger: telnet:` entry whose pname key does not name any processor of the device in the current build context."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:495-498", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:490-491", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:482-483"]
---

## Symptom

`pname '<…>' does not match any device pname`

## Cause

The csolution YAML has a `debugger: telnet:` entry whose pname key does not name any processor of the device in the current build context. The pnames map is built from the device's processors; the telnet key is taken from the user's debugger telnet definitions. The placeholder in the message is that key as the user wrote it. The entry is skipped and the build continues with a warning.

## Fix

Check the telnet entry in the csolution YAML (under the debugger/telnet section of the project or context). Make its key equal to a processor name of the selected device, for example a pname as listed in the device's processor definitions in the PDSC. If the entry is not needed, remove it.

## Trigger in the source

```cpp
if (pnames.find(pname) == pnames.end()) {
```

## Note

The README does not document this message. The check at line 495 runs after the multicore check at line 491, so a multi-core device with an empty telnet pname is reported by the earlier message instead. The fix assumes the device's pnames are the valid keys, which the code implies through the pnames map argument.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:495-498`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:490-491`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:482-483`
