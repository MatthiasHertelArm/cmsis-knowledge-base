---
id: "ts-csolution-redefinition-from-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefinition from '…' into '…'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["redefinition from '<…>' into '<…>'"]
symptom_regex: "^redefinition from '.+?' into '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3005"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3000", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3099", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:151", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4798"]
---

## Symptom

`redefinition from '<…>' into '<…>'`

## Cause

The compiler selected on the command line with `-t`/`--toolchain` differs from the `compiler:` that the YAML files set for the context; the first `<…>` is the YAML compiler, the second the command-line one. The command line wins, and the context is built with that compiler.

## Fix

No change is needed if the override is intended. Otherwise drop `-t`, or pass the compiler the YAML sets (e.g. `-t AC6`), or change `compiler:` in the csolution.yml.

## Trigger in the source

```cpp
if (acceptRedefinition) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3000`
- `tools/projmgr/src/ProjMgrWorker.cpp:3099`
- `tools/projmgr/src/ProjMgrUtils.cpp:151`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4798`
