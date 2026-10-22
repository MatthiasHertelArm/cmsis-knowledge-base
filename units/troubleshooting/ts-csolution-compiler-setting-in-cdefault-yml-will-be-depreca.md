---
id: "ts-csolution-compiler-setting-in-cdefault-yml-will-be-depreca"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: 'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0"]
symptom_regex: "^'compiler' setting in cdefault\\.yml will be deprecated in CMSIS\\-Toolbox 3\\.0\\.0$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:45"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The cdefault.yml file sets a top-level default 'compiler' key."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:43-46", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:47"]
---

## Symptom

`'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0`

## Cause

The cdefault.yml file sets a top-level default 'compiler' key. ParseCdefault reads that value and, when it is non-empty, prints this warning. The message says the setting is deprecated and will be removed in CMSIS-Toolbox 3.0.0; the build still uses the value for this run.

## Fix

Remove the 'compiler' entry from the default section of cdefault.yml and use the selectable compiler settings that ParseSelectableCompilers reads from the same node instead. The source shown does not spell out the exact replacement YAML keys, so check the cdefault.yml schema of your CMSIS-Toolbox version before editing.

## Trigger in the source

```cpp
if (!cdefault.compiler.empty()) {
```

## Note

The README does not document this message. The warning is printed at parse time, so it appears whenever a cdefault.yml sets 'compiler'. The replacement mechanism is inferred from the line that follows the warning and is not confirmed by the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:43-46`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:47`
