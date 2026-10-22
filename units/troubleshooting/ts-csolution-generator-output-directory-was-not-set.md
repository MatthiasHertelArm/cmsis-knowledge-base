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
summary: "The csolution tool resolves the output directory of an external generator in GetExtGeneratorOptions."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5688-5699", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5705-5741"]
---

## Symptom

`generator output directory was not set`

## Cause

The csolution tool resolves the output directory of an external generator in GetExtGeneratorOptions. It takes the path from the 'generators' node of the layer, project or solution (a path set for that generator id, or a baseDir), and if that is empty it falls back to the global generator register by generator id. If the result is still empty, the tool logs this error and stops. This means the generator used by the project has no output directory: neither the generators node in the csolution or cproject YAML sets one, nor the generator's global registration provides one.

## Fix

Give the generator an output directory in the csolution YAML, for example under a 'generators' node of the project or solution: set a path for the generator id, or set a baseDir so the tool builds the path from the generator id. Then run the build again. If the generator is supposed to be registered globally, check that its global registration (done by the generator's own installation) provides a path.

## Trigger in the source

```cpp
if (options.path.empty()) {
```

## Note

The README does not document this message. The cause is inferred from the code path that resolves the generator directory; the exact YAML keys for the generators node are taken from GetGeneratorOptions and were not checked against the schema. The global register lookup is in m_extGenerator->GetGlobalGenDir, which is outside the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5688-5699`
- `tools/projmgr/src/ProjMgrWorker.cpp:5705-5741`
