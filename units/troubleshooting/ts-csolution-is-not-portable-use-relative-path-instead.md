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
summary: "A path value in a csolution.yml, cproject.yml or clayer.yml (projects:, layers:, files:, add-path:, linker:, packs: path:, output-dirs:, generators: and similar path nodes) is absolute, e.g."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:337-340", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:355-367", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4431", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5455-5461", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/Portability/portability.csolution.yml"]
---

## Symptom

`absolute path '<…>' is not portable, use relative path instead`

## Cause

A path value in a csolution.yml, cproject.yml or clayer.yml (projects:, layers:, files:, add-path:, linker:, packs: path:, output-dirs:, generators: and similar path nodes) is absolute, e.g. `/home/user/...` or `C:/...`. The `<…>` is that path; the message carries file, line and column.

## Fix

Write the path relative to the YAML file that contains it (e.g. `../common/inc`), or use an access sequence such as `$SolutionDir()$/common/inc`, so the project works on other machines.

## Trigger in the source

```cpp
if (fs::path(value).is_absolute()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:337-340`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:355-367`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4431`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5455-5461`
- `tools/projmgr/test/data/TestSolution/Portability/portability.csolution.yml`
