---
id: "ts-csolution-uses-unknown-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: …Component … uses unknown generator …"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["<…>Component <…> uses unknown generator <…>"]
symptom_regex: "^.+?Component .+? uses unknown generator .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrCbuild.cpp:179"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The component's generator ID (the generator attribute of the component selection in the csolution YAML) is neither a generator found in the loaded packs (context->generators, and not external) nor an external generator registered in context->extGen."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:166-180", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:168-169", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:174", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:179"]
---

## Symptom

`<…>Component <…> uses unknown generator <…>`

## Cause

The component's generator ID (the generator attribute of the component selection in the csolution YAML) is neither a generator found in the loaded packs (context->generators, and not external) nor an external generator registered in context->extGen. The first part of the message is the component ID, and the last part is the generator ID the user or pack referenced. The warning is printed from SetComponentsNode when generating the cbuild file, and the component's generator entry is still written with just its ID.

## Fix

Check the generator ID spelling against the generator IDs declared in the installed packs, and make sure the pack that declares that generator is listed in the project's packs or installed in the environment (for example by running cpackget add or by fixing the pack reference in the csolution YAML). If the generator is meant to be external, declare it in the project's external generator configuration so it is registered in context->extGen.

## Trigger in the source

```cpp
} else if (contains_key(context->extGen, component.generator)) {
```

## Note

Not documented in the README. The message is a warning, so the cbuild file is still written; the cause and fix are my reading of the branch conditions, and the external-generator registration step is not shown in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrCbuild.cpp:166-180`
- `tools/projmgr/src/ProjMgrCbuild.cpp:168-169`
- `tools/projmgr/src/ProjMgrCbuild.cpp:174`
- `tools/projmgr/src/ProjMgrCbuild.cpp:179`
