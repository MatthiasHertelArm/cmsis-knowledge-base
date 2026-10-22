---
id: "ts-csolution-generator-output-directory-was-not-set"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator output directory was not set"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator output directory was not set"]
symptom_regex: "^generator output directory was not set$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5697"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A selected component uses a globally registered generator, and no output folder is known for it: no `generators: options: - generator: <id> path:` and no `generators: base-dir:` in the clayer.yml, cproject.yml or csolution.yml, and no `path:` in the generator's …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5683-5703", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5705-5740", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5843-5867", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/ExternalGenerator/no-gendir.generator.yml"]
---

## Symptom

`generator output directory was not set`

## Cause

A selected component uses a globally registered generator, and no output folder is known for it: no `generators: options: - generator: <id>  path:` and no `generators: base-dir:` in the clayer.yml, cproject.yml or csolution.yml, and no `path:` in the generator's global registration (*.generator.yml).

## Fix

Set the folder in the cproject.yml (or csolution.yml), e.g. `generators: options: - generator: CubeMX  path: ./CubeMX`, or set `generators: base-dir: ./generated`.

## Trigger in the source

```cpp
if (options.path.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5683-5703`
- `tools/projmgr/src/ProjMgrWorker.cpp:5705-5740`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5843-5867`
- `tools/projmgr/test/data/ExternalGenerator/no-gendir.generator.yml`
