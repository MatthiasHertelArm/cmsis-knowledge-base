---
id: "ts-csolution-is-declared-multiple-times"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: group '…' is declared multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: group '<…>' is declared multiple times"]
symptom_regex: "^conflict: group '.+?' is declared multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3835"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Two groups with the same `group:` name sit at the same level for one context."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3801-3847", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5929-5934", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/ExternalGenerator/single/wrong.cproject.yml", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/ExternalGenerator/single/generated/wrong.cgen.yml"]
---

## Symptom

`conflict: group '<…>' is declared multiple times`

## Cause

Two groups with the same `group:` name sit at the same level for one context. Top-level groups of the cproject.yml, of all its clayer.yml files and of a generator's *.cgen.yml are merged into one list, so a name used in the project and in a layer or generated file collides; nested groups are compared within their parent group.

## Fix

Rename one of the groups (e.g. `group: App Sources` vs `group: Board Sources`), or give them disjoint `for-context:` filters.

## Trigger in the source

```cpp
if (dstNode.group == src.group) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3801-3847`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5929-5934`
- `tools/projmgr/test/data/ExternalGenerator/single/wrong.cproject.yml`
- `tools/projmgr/test/data/ExternalGenerator/single/generated/wrong.cgen.yml`
