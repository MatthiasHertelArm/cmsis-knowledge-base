---
id: "ts-csolution-is-not-portable-use-relative-path-instead"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: absolute path '…' is not portable, use relative path instead"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["absolute path '<…>' is not portable, use relative path instead"]
symptom_regex: "^absolute path '.+?' is not portable, use relative path instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:339"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "EnsurePortability runs on path-valued csolution YAML entries (through ParsePortablePath and ParsePortablePaths)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:333-339", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:355-358", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:361-367"]
---

## Symptom

`absolute path '<…>' is not portable, use relative path instead`

## Cause

EnsurePortability runs on path-valued csolution YAML entries (through ParsePortablePath and ParsePortablePaths). When the value is an absolute path, fs::path(value).is_absolute() is true and the tool emits this warning with the offending value in place of the placeholder. The warning is not an error; the build keeps the path as written, but it will not resolve the same on another machine or in a different checkout.

## Fix

Replace the absolute path in the YAML entry with a path relative to the file that contains it, for example change an absolute directory to a path such as ../lib or ./Source, so that it resolves from the project file location. Re-run csolution to confirm the warning is gone.

## Trigger in the source

```cpp
if (fs::path(value).is_absolute()) {
```

## Note

The warning is emitted with Warn, not Error, so processing continues. The message text is the absolute path '<…>' (the variable part is the raw YAML value). The same function also emits the backslash and case-inconsistency warnings for the same entries; those are distinct messages.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:333-339`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:355-358`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:361-367`
