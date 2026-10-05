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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:335"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:332-336", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:355-367", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:785", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:800", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:845", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:893", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:987", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1026", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1083", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5411-5441", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/Portability/portability.csolution.yml"]
---

## Symptom

`'<…>' contains non-portable backslash, use forward slash instead`

## Cause

A path value in a csolution.yml, cproject.yml or clayer.yml contains a backslash, for example under projects: project:, layers: layer:, files: file:, add-path:, linker: script:/regions:, packs: path:, output-dirs: or generators:. The `<…>` is the path as written; the message is prefixed with the YAML file, line and column.

## Fix

Write the path with forward slashes, e.g. `- file: ../src/main.c` instead of `..\src\main.c`; forward slashes work on Windows, Linux and macOS.

## Trigger in the source

```cpp
if (value.find('\\') != string::npos) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:332-336`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:355-367`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:785`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:800`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:845`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:893`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:987`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1026`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1083`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5411-5441`
- `tools/projmgr/test/data/TestSolution/Portability/portability.csolution.yml`
