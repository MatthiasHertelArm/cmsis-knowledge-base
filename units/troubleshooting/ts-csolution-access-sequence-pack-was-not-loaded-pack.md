---
id: "ts-csolution-access-sequence-pack-was-not-loaded-pack"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: access sequence pack was not loaded: '$Pack(…)$'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["access sequence pack was not loaded: '$Pack(<…>)$'"]
symptom_regex: "^access sequence pack was not loaded: '\\$Pack\\(.+?\\)\\$'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3703"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `$Pack(Vendor::Name)$` access sequence refers to a pack that is not among the packs loaded for the context: it is not listed under packs: of the csolution.yml/cproject.yml/clayer.yml (when packs are listed, only those are loaded) or it is not installed."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3684-3707", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:539-575", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2666-2691", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestAccessSequences/pack-access-sequences.csolution.yml:12"]
---

## Symptom

`access sequence pack was not loaded: '$Pack(<…>)$'`

## Cause

A `$Pack(Vendor::Name)$` access sequence refers to a pack that is not among the packs loaded for the context: it is not listed under packs: of the csolution.yml/cproject.yml/clayer.yml (when packs are listed, only those are loaded) or it is not installed. The `<…>` is the pack as written; the sequence stays unexpanded, so the resulting path is wrong.

## Fix

Add the pack to packs:, e.g. `- pack: ARM::CMSIS`, and install it with `cpackget add Vendor::Name`; or correct the vendor/name spelling in the `$Pack(...)$` sequence.

## Trigger in the source

```cpp
if (replacement.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3684-3707`
- `tools/projmgr/src/ProjMgrWorker.cpp:539-575`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2666-2691`
- `tools/projmgr/test/data/TestAccessSequences/pack-access-sequences.csolution.yml:12`
