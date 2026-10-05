---
id: "ts-csolution-valid-tracebuffer-elements-must-be-named-when-mo"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: valid <tracebuffer> elements must be named when more than one is declared"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["valid <tracebuffer> elements must be named when more than one is declared"]
symptom_regex: "^valid <tracebuffer> elements must be named when more than one is declared$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:608"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The device description in the DFP declares several `<tracebuffer>` elements in its device-wide `<trace>` section and at least one of them has no `name` attribute, so the trace sinks written to the cbuild-run.yml cannot be told apart."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:587", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:607", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:233", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7166"]
---

## Symptom

`valid <tracebuffer> elements must be named when more than one is declared`

## Cause

The device description in the DFP declares several `<tracebuffer>` elements in its device-wide `<trace>` section and at least one of them has no `name` attribute, so the trace sinks written to the cbuild-run.yml cannot be told apart. It is a flaw of the pack, not of the project.

## Fix

Nothing to change in the project; the run and debug files are still written. Report the unnamed `<tracebuffer>` to the DFP vendor or update to a DFP version that names them.

## Trigger in the source

```cpp
if (traceBufferCount > 1 && unnamedTraceBufferCount > 0) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:587`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:607`
- `test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:233`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7166`
