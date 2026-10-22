---
id: "ts-csolution-manifest-file-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: manifest file does not exist"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["manifest file does not exist"]
symptom_regex: "^manifest file does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:1215"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "GetToolboxVersion searches the CMSIS-Toolbox directory (the toolboxDir argument, from GetCmsisToolboxDir) non-recursively for a file matching manifest_<major.minor.patch>*.yml."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1214-1217", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1184-1188", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1185"]
---

## Symptom

`manifest file does not exist`

## Cause

GetToolboxVersion searches the CMSIS-Toolbox directory (the toolboxDir argument, from GetCmsisToolboxDir) non-recursively for a file matching manifest_<major.minor.patch>*.yml. This is reached only when a csolution file has a created-for entry naming cmsis-toolbox at a version; ValidateCreatedFor calls GetToolboxVersion to compare that version with the installed toolbox. If no such manifest file is in the toolbox directory, the version cannot be determined and the check is skipped. The path shown in the message is the toolbox directory that was searched.

## Fix

Check that the toolbox directory shown in the message contains a manifest_<version>.yml file of the installed CMSIS-Toolbox. If the toolbox installation is incomplete or was not set up correctly, reinstall or repair it so that the manifest file is present. If the created-for entry in the csolution file is not needed, remove it so this check is not run.

## Trigger in the source

```cpp
if (!RteFsUtils::FindFileWithPattern(toolboxDir, manifestFilePattern, manifestFile)) {
```

## Note

The warning is not fatal: GetToolboxVersion returns an empty string and ValidateCreatedFor then returns true, so processing continues without the version comparison. The cause and fix are inferred from the code path; the README does not document this message. The reference to removing created-for is a workaround I derived from the code, not an officially documented remedy.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1214-1217`
- `tools/projmgr/src/ProjMgr.cpp:1184-1188`
- `tools/projmgr/src/ProjMgr.cpp:1185`
