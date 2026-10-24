---
id: "ts-csolution-uses-unknown-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: …Component … uses unknown generator …"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["<…>Component <…> uses unknown generator <…>"]
symptom_regex: "^.+?Component .+? uses unknown generator .*$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrCbuild.cpp:179"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "While writing the cbuild.yml, a selected component names a generator (`generator` attribute of the component, possibly a component inserted from a generator's gpdsc file) that is neither a generator defined in its pack nor a generator registered in the …"
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:165-179", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2049-2080", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2918-2937", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteComponent.cpp:311-325"]
---

## Symptom

`<…>Component <…> uses unknown generator <…>`

## Cause

While writing the cbuild.yml, a selected component names a generator (`generator` attribute of the component, possibly a component inserted from a generator's gpdsc file) that is neither a generator defined in its pack nor a generator registered in the global generator register (*.generator.yml in the CMSIS-Toolbox etc folder). The cbuild.yml then lacks the generator's from-pack or path entry.

## Fix

Check that the generator id in the pack or gpdsc matches a `<generator id=...>` of the pack, or that the external generator is registered in a *.generator.yml in <cmsis-toolbox>/etc; then re-run the generator (`csolution run <name>.csolution.yml -g <generator-id> -c <context>`) so that a consistent gpdsc is written.

## Trigger in the source

```cpp
} else if (contains_key(context->extGen, component.generator)) {
```

## Note

For components of the project itself, ProcessComponents already fails with 'was not found in global register', so the warning can only come from components added later (gpdsc components); no test reproduces it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgrCbuild.cpp:165-179`
- `tools/projmgr/src/ProjMgrWorker.cpp:2049-2080`
- `tools/projmgr/src/ProjMgrWorker.cpp:2918-2937`
- `libs/rtemodel/src/RteComponent.cpp:311-325`
