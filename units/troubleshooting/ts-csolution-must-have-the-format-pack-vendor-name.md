---
id: "ts-csolution-must-have-the-format-pack-vendor-name"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: access sequence '$Pack(…)' must have the format '$Pack(vendor::name)$'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["access sequence '$Pack(<…>)' must have the format '$Pack(vendor::name)$'"]
symptom_regex: "^access sequence '\\$Pack\\(.+?\\)' must have the format '\\$Pack\\(vendor::name\\)\\$'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3688"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `$Pack(...)$` access sequence in a YAML path or option has an argument without both vendor and pack name separated by `::`, e.g."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3684-3690", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3727-3729", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2667-2691", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestAccessSequences/pack-access-sequences.csolution.yml:13"]
---

## Symptom

`access sequence '$Pack(<…>)' must have the format '$Pack(vendor::name)$'`

## Cause

A `$Pack(...)$` access sequence in a YAML path or option has an argument without both vendor and pack name separated by `::`, e.g. `$Pack(Wrong.Format)$`. The `<…>` is the argument; the sequence is left unexpanded.

## Fix

Write the pack as `$Pack(Vendor::Name)$`, e.g. `$Pack(ARM::CMSIS)$/CMSIS/Include`.

## Trigger in the source

```cpp
if (packInfo.vendor.empty() || packInfo.name.empty()) {
```

## Note

The message prints the given sequence without its closing '$'.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3684-3690`
- `tools/projmgr/src/ProjMgrWorker.cpp:3727-3729`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2667-2691`
- `tools/projmgr/test/data/TestAccessSequences/pack-access-sequences.csolution.yml:13`
