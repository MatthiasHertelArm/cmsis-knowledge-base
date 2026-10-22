---
id: "ts-csolution-contains-non-portable-backslash-use-forward-slas"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' contains non-portable backslash, use forward slash instead"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' contains non-portable backslash, use forward slash instead"]
symptom_regex: "^'.+?' contains non\\-portable backslash, use forward slash instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:335"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution parser checks every path-valued YAML entry (parsed through ParsePortablePath or ParsePortablePaths) for a backslash character."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:334-335", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:355-358", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:361-367"]
---

## Symptom

`'<…>' contains non-portable backslash, use forward slash instead`

## Cause

The csolution parser checks every path-valued YAML entry (parsed through ParsePortablePath or ParsePortablePaths) for a backslash character. The warning fires when the value of a path key in the csolution YAML files, such as a file, include or directory entry, contains a Windows-style backslash separator. The placeholder in the message is that offending value, copied verbatim from the YAML.

## Fix

Edit the YAML entry that the warning points to (file and line are given in the log) and replace each backslash with a forward slash, for example write src/main.c instead of src\main.c. Forward slashes work on all host systems, so the project stays portable between Windows and Linux.

## Trigger in the source

```cpp
if (value.find('\\') != string::npos) {
```

## Note

The message is a warning, not an error, so the build continues. The code is empty in the message, so the id carries no code. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:334-335`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:355-358`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:361-367`
