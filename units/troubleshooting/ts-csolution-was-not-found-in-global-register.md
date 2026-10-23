---
id: "ts-csolution-was-not-found-in-global-register"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator '…' required by component '…' was not found in global register"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator '<…>' required by component '<…>' was not found in global register"]
symptom_regex: "^generator '.+?' required by component '.+?' was not found in global register$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrExtGenerator.cpp:35"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A selected component names a generator that its pack does not define and that is not registered globally: no *.generator.yml in the CMSIS-Toolbox etc folder has an entry with that `id:`."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:29-40", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2065-2072", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteKernel.cpp:256-280", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:1945", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5793-5809"]
---

## Symptom

`generator '<…>' required by component '<…>' was not found in global register`

## Cause

A selected component names a generator that its pack does not define and that is not registered globally: no *.generator.yml in the CMSIS-Toolbox etc folder has an entry with that `id:`. Typical for components that rely on an external tool such as STM32CubeMX when the installation lacks its registration file. The `<…>` are the generator id and the component.

## Fix

Use a CMSIS-Toolbox installation whose etc folder contains the generator's *.generator.yml (an entry `generator: - id: <id>  run: ...  path: ...`), or remove the component that needs it.

## Trigger in the source

```cpp
if (!IsGlobalGenerator(generatorId)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrExtGenerator.cpp:29-40`
- `tools/projmgr/src/ProjMgrWorker.cpp:2065-2072`
- `libs/rtemodel/src/RteKernel.cpp:256-280`
- `tools/projmgr/schemas/common.schema.json:1945`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5793-5809`
