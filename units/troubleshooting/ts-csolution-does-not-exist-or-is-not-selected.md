---
id: "ts-csolution-does-not-exist-or-is-not-selected"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' referenced by access sequence '…' does not exist or is not selected"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' referenced by access sequence '<…>' does not exist or is not selected"]
symptom_regex: "^context '.+?' referenced by access sequence '.+?' does not exist or is not selected$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3777"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3752-3781", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:459-490", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2634-2664", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestAccessSequences/test-not_exisitng-access-sequences1.cproject.yml:9", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestAccessSequences/test-not_exisitng-access-sequences2.cproject.yml:11"]
---

## Symptom

`context '<…>' referenced by access sequence '<…>' does not exist or is not selected`

## Cause

An access sequence with a context argument in a cproject.yml or clayer.yml, such as `$elf(project.Debug+Target)$`, `$cmse-lib(...)$`, `$OutDir(...)$` or `$ProjectDir(...)$`, refers to a context that is not among the contexts selected for this run: the project, build type or target type is misspelled, or that context is excluded by `-c`, `--active` or the cbuild-set. Omitted project or target parts default to those of the current context. The `<…>` are the referenced context and the sequence name.

## Fix

Correct the context name in the access sequence (`csolution list contexts <name>.csolution.yml` lists them) and make sure the referenced context is built in the same run, e.g. select it with an additional `-c <context>` or add it to the target-set.

## Trigger in the source

```cpp
if (genDep && refContext.name != context.name) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3752-3781`
- `tools/projmgr/src/ProjMgrUtils.cpp:459-490`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2634-2664`
- `tools/projmgr/test/data/TestAccessSequences/test-not_exisitng-access-sequences1.cproject.yml:9`
- `tools/projmgr/test/data/TestAccessSequences/test-not_exisitng-access-sequences2.cproject.yml:11`
