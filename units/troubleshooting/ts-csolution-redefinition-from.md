---
id: "ts-csolution-redefinition-from"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefinition from '…' into '…' is not allowed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["redefinition from '<…>' into '<…>' is not allowed"]
symptom_regex: "^redefinition from '.+?' into '.+?' is not allowed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:797"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A setting that takes a single value is given two different values for the same context at different places (csolution.yml, a target-type or build-type, cproject.yml, a setup or a clayer.yml); the first `<…>` is the value found first, the …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:794", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2991", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3040", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3164", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/toolchain-redefinition.csolution.yml:5", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4787", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4701", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1504"]
---

## Symptom

`redefinition from '<…>' into '<…>' is not allowed`

## Cause

A setting that takes a single value is given two different values for the same context at different places (csolution.yml, a target-type or build-type, cproject.yml, a setup or a clayer.yml); the first `<…>` is the value found first, the second the conflicting one. It applies to the parts of `board:` and `device:` (vendor, name, revision or processor), `compiler:` (different names or versions that do not overlap), `optimize:`, `debug:`, `warnings:`, `language-C:`, `language-CPP:`, the `processor:` options, the `linker:` script and regions file, and `output:` - `base-name:`.

## Fix

Set the value in one place only, or make the values agree; restrict a differing setting with `for-context:` so that only one applies to each context. For the compiler, a version range such as `AC6@>=6.18` combines with `AC6`; `AC6` and `GCC` do not.

## Trigger in the source

```cpp
if (!outValue.empty() && (outValue != element)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:794`
- `tools/projmgr/src/ProjMgrWorker.cpp:2991`
- `tools/projmgr/src/ProjMgrWorker.cpp:3040`
- `tools/projmgr/src/ProjMgrWorker.cpp:3164`
- `tools/projmgr/test/data/TestSolution/toolchain-redefinition.csolution.yml:5`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4787`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4701`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1504`
