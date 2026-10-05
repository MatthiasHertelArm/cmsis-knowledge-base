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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1215"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1209", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1184", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrKernel.cpp:36", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7104"]
---

## Symptom

`manifest file does not exist`

## Cause

The csolution.yml has `created-for: CMSIS-Toolbox@<version>`, and to compare versions csolution looks for `manifest_<x.y.z>*.yml` in the CMSIS-Toolbox installation directory (the parent of the folder that holds the csolution executable). No such file is there, so the minimum-version check is skipped.

## Fix

Use csolution from a complete CMSIS-Toolbox installation, whose root folder contains the manifest file; reinstall the toolbox if it is missing. The warning does not stop the run.

## Trigger in the source

```cpp
if (!RteFsUtils::FindFileWithPattern(toolboxDir, manifestFilePattern, manifestFile)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1209`
- `tools/projmgr/src/ProjMgr.cpp:1184`
- `tools/projmgr/src/ProjMgrKernel.cpp:36`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7104`
