---
id: "ts-csolution-more-than-one-valid-serialwire-element-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: more than one valid <serialwire> element found"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["more than one valid <serialwire> element found"]
symptom_regex: "^more than one valid <serialwire> element found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrRunDebug.cpp:605"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The device description in the DFP has more than one `<serialwire>` element in its `<trace>` sections that apply to the whole device (trace elements with a Pname attribute are ignored). csolution writes only one serial-wire trace sink into the cbuild-run.yml."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:575", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:604", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:229", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7165"]
---

## Symptom

`more than one valid <serialwire> element found`

## Cause

The device description in the DFP has more than one `<serialwire>` element in its `<trace>` sections that apply to the whole device (trace elements with a Pname attribute are ignored). csolution writes only one serial-wire trace sink into the cbuild-run.yml. It is a flaw of the pack, not of the project.

## Fix

Nothing to change in the project; the run and debug files are still written. Report the duplicate `<serialwire>` to the DFP vendor or update to a DFP version that fixes it.

## Trigger in the source

```cpp
if (serialWireCount > 1) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:575`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:604`
- `test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:229`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7165`
