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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrExtGenerator.cpp:35"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A component in the csolution project or its packs names a code generator by id, and the csolution tool cannot find a generator with that id in its global generator register."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:29-31", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:34-37"]
---

## Symptom

`generator '<…>' required by component '<…>' was not found in global register`

## Cause

A component in the csolution project or its packs names a code generator by id, and the csolution tool cannot find a generator with that id in its global generator register. The lookup goes through ProjMgrKernel's external generator table, which is populated from installed packs and the CMSIS environment; a generator id that is not registered there fails the check. The first quoted value is the generator id from the component, the second is the component id that requires it.

## Fix

Check the generator id spelled in the component's generator reference against the generator ids the installed packs declare, and correct the spelling if it differs. If the generator comes from a pack, make sure that pack is installed and selected in the project so that its generator is registered before the build runs, for example by running cpackget to install the pack and then rebuilding.

## Trigger in the source

```cpp
if (!IsGlobalGenerator(generatorId)) {
```

## Note

The source confirms the trigger, which is a failed lookup in the kernel's external generator table. The user-facing cause (misspelled id or missing pack) is my reading of how that table is filled; the lines given do not show where the table is populated. The message is printed with severity error and no README entry exists for it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrExtGenerator.cpp:29-31`
- `tools/projmgr/src/ProjMgrExtGenerator.cpp:34-37`
