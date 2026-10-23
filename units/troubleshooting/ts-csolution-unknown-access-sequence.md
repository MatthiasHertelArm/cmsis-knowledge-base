---
id: "ts-csolution-unknown-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: unknown access sequence: '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["unknown access sequence: '<…>'"]
symptom_regex: "^unknown access sequence: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3783"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A value contains `$<name>$` or `$<name>(<arg>)$` that is neither a defined variable nor a known access sequence; `<…>` is the text between the `$` signs."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3783", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:21", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:238", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3112", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/ExternalGenerator/wrong-gendir.generator.yml:5", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/MLOps/failure_image_only_hw.csolution.yml:18", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5834"]
---

## Symptom

`unknown access sequence: '<…>'`

## Cause

A value contains `$<name>$` or `$<name>(<arg>)$` that is neither a defined variable nor a known access sequence; `<…>` is the text between the `$` signs. Known ones include `$Dname$`, `$Pname$`, `$Bname$`, `$Compiler$`, `$Solution$`, `$Project$`, `$BuildType$`, `$TargetType$`, `$TargetSet$`, `$Dpack$`, `$Bpack$`, `$SolutionDir()$`, `$ProjectDir(<context>)$`, `$OutDir(<context>)$`, `$elf()$`, `$bin()$`, `$hex()$`, `$lib()$`, `$map()$`, `$cmse()$` and `$Pack(<pack>)$`, plus variables from `variables:`. Example: `path: $UnknownAccessSequence()$` in a generator file.

## Fix

Correct the spelling or case of the access sequence, or define the variable under `variables:` of the target type or build type in the csolution.yml.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3783`
- `tools/projmgr/src/ProjMgrWorker.cpp:21`
- `tools/projmgr/src/ProjMgrWorker.cpp:238`
- `tools/projmgr/src/ProjMgrWorker.cpp:3112`
- `tools/projmgr/test/data/ExternalGenerator/wrong-gendir.generator.yml:5`
- `tools/projmgr/test/data/MLOps/failure_image_only_hw.csolution.yml:18`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5834`
