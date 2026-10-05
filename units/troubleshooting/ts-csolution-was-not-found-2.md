---
id: "ts-csolution-was-not-found-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator '<…>' was not found"]
symptom_regex: "^generator '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5113"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5106-5115", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1056-1066", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2053-2056"]
---

## Symptom

`generator '<…>' was not found`

## Cause

The id given with `csolution run -g <id>` matches neither a globally registered generator nor a generator of a component selected in the context. Ids are case-sensitive and come from the pack's `<generator id=...>`.

## Fix

List valid ids with `csolution list generators <name>.csolution.yml -c <context>` and pass one of them; check that the component that uses the generator is in the context's components:.

## Trigger in the source

```cpp
if (generators.find(generatorId) == generators.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5106-5115`
- `tools/projmgr/src/ProjMgr.cpp:1056-1066`
- `tools/projmgr/src/ProjMgrWorker.cpp:2053-2056`
