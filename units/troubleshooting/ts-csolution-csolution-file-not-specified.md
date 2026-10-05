---
id: "ts-csolution-csolution-file-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: csolution file not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["csolution file not specified"]
symptom_regex: "^csolution file not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:537"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257-266", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:536-539", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5170-5178"]
---

## Symptom

`csolution file not specified`

## Cause

The command needs a solution, but none was given: no `--solution`/`-s` option and no positional argument whose name ends in `.csolution.yml` or `.csolution.yaml`. A file with another name is not recognized as the solution.

## Fix

Pass the solution file, e.g. `csolution convert my.csolution.yml` or `csolution list configs -s my.csolution.yml`; rename the file to `<name>.csolution.yml` if needed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:257-266`
- `tools/projmgr/src/ProjMgr.cpp:536-539`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5170-5178`
