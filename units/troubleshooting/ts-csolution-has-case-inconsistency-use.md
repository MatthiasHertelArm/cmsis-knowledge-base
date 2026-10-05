---
id: "ts-csolution-has-case-inconsistency-use"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' has case inconsistency, use '…' instead"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' has case inconsistency, use '<…>' instead"]
symptom_regex: "^'.+?' has case inconsistency, use '.+?' instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:347"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:337-350", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5444-5453", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5346-5356"]
---

## Symptom

`'<…>' has case inconsistency, use '<…>' instead`

## Cause

A relative path in a csolution.yml, cproject.yml or clayer.yml points to an existing file or folder, but its upper/lower case differs from the name on disk. It only shows on case-insensitive file systems (Windows, default macOS), where the path still resolves; on Linux the same path is not found. The first `<…>` is the path as written, the second the path with the case on disk, relative to the YAML file.

## Fix

Replace the path with the suggested spelling, e.g. `- layer: ../layer.clayer.yml` instead of `../laYer.clayer.yml`, so the project also builds on case-sensitive hosts such as Linux CI runners.

## Trigger in the source

```cpp
if (!canonical.empty() && (original != canonical)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:337-350`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5444-5453`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5346-5356`
