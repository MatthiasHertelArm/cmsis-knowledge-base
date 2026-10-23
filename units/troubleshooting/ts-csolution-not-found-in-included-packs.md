---
id: "ts-csolution-not-found-in-included-packs"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: component '…' not found in included packs… did you mean '…'?…"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["component '<…>' not found in included packs<…>\n  did you mean '<…>'?<…>"]
symptom_regex: "^component '.+?' not found in included packs.+?\\\n  did you mean '.+?'\\?.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:2001"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `component:` entry matches no component that the loaded packs offer for this context."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1990-2008", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2183-2280", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:539-541", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1515-1523", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5924-5928"]
---

## Symptom

`component '<…>' not found in included packs<…>
  did you mean '<…>'?<…>`

## Cause

A `component:` entry matches no component that the loaded packs offer for this context. Either the pack is not listed under packs:/not installed, the ID is misspelled or incomplete (Cclass:Cgroup:Csub, `&Cvariant`, vendor `::`), the version after `@` matches no available version, or the component's pack condition excludes the device, board or compiler. When exactly one component matches partially, the message adds `did you mean '<id>'`.

## Fix

Use the suggested ID if one is shown; otherwise run `csolution list components <name>.csolution.yml -c <context>` to see what is available and copy the ID, and add the missing pack under packs: (then `cpackget add Vendor::PackName`).

## Trigger in the source

```cpp
if (!matchedComponent) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1990-2008`
- `tools/projmgr/src/ProjMgrWorker.cpp:2183-2280`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:539-541`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1515-1523`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5924-5928`
