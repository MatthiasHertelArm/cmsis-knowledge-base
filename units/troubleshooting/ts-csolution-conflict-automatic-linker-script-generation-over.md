---
id: "ts-csolution-conflict-automatic-linker-script-generation-over"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: automatic linker script generation overrules specified script '…'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["conflict: automatic linker script generation overrules specified script '<…>'"]
symptom_regex: "^conflict: automatic linker script generation overrules specified script '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2359"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The context has `linker: - auto:` and also a linker script from `linker: - script:` (in the cproject.yml, a clayer.yml or a setup)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2354-2361", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3555-3575", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4893-4901"]
---

## Symptom

`conflict: automatic linker script generation overrules specified script '<…>'`

## Cause

The context has `linker: - auto:` and also a linker script from `linker: - script:` (in the cproject.yml, a clayer.yml or a setup). Automatic linker script generation wins and the named script, shown in `<…>`, is dropped.

## Fix

Keep one of the two: remove `auto:` to use your script, or remove `script:` to use the generated one; or restrict either entry with `for-context:`/`for-compiler:`.

## Trigger in the source

```cpp
if (!context.linker.script.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2354-2361`
- `tools/projmgr/src/ProjMgrWorker.cpp:3555-3575`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4893-4901`
