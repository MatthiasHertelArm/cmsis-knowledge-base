---
id: "ts-csolution-input-csolution-yml-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: input csolution.yml was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["input csolution.yml was not specified"]
symptom_regex: "^input csolution\\.yml was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1076"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1074", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:266", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:455", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:675"]
---

## Symptom

`input csolution.yml was not specified`

## Cause

`csolution check pack-updates` was run without a solution file. The command needs the *.csolution.yml either with `-s`/`--solution` or as a positional argument whose name ends in `.csolution.yml` (or `.csolution.yaml`); a file with any other name is not recognised as the solution.

## Fix

Pass the solution file: `csolution check pack-updates my.csolution.yml` or `csolution check pack-updates -s path/to/my.csolution.yml`. Rename the file to `<name>.csolution.yml` if it does not follow that pattern.

## Trigger in the source

```cpp
if (m_csolutionFile.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1074`
- `tools/projmgr/src/ProjMgr.cpp:257`
- `tools/projmgr/src/ProjMgr.cpp:266`
- `tools/projmgr/src/ProjMgr.cpp:455`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:675`
