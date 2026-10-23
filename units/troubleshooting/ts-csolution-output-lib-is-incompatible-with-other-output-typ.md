---
id: "ts-csolution-output-lib-is-incompatible-with-other-output-typ"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: output 'lib' is incompatible with other output types"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["output 'lib' is incompatible with other output types"]
symptom_regex: "^output 'lib' is incompatible with other output types$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:5611"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The `output:` - `type:` settings that apply to a context combine `lib` with `elf`, `hex` or `bin`; output types from several `output:` nodes (in cproject.yml, setups, clayer.yml) add up."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5608", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/outputFiles.cproject.yml:2", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4703"]
---

## Symptom

`output 'lib' is incompatible with other output types`

## Cause

The `output:` - `type:` settings that apply to a context combine `lib` with `elf`, `hex` or `bin`; output types from several `output:` nodes (in cproject.yml, setups, clayer.yml) add up. Example: a setup with `type: [elf, hex, bin, map]` and another with `type: lib` that both match the same build type.

## Fix

Make each context build either a library or an executable: restrict the `output:` nodes with `for-context:`/`not-for-context:` so that `type: lib` never meets `elf`, `hex` or `bin`.

## Trigger in the source

```cpp
if (context.outputTypes.lib.on &&
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5608`
- `tools/projmgr/test/data/TestSolution/outputFiles.cproject.yml:2`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4703`
