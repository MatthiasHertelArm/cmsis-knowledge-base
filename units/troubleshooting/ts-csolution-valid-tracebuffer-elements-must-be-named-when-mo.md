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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrRunDebug.cpp:608"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The device's effective trace properties contain more than one valid <tracebuffer> sink (counted from the <trace> children that have no Pname attribute), and at least one of them has an empty or missing name attribute."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:575-579", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:582-584", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:592-600", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRunDebug.cpp:607-608"]
---

## Symptom

`valid <tracebuffer> elements must be named when more than one is declared`

## Cause

The device's effective trace properties contain more than one valid <tracebuffer> sink (counted from the <trace> children that have no Pname attribute), and at least one of them has an empty or missing name attribute. The tool counts every tracebuffer and every unnamed one, and warns when the count exceeds one with any unnamed entry present, because unnamed trace buffers cannot be told apart when the debugger's trace sinks are collected.

## Fix

Give each <tracebuffer> element that the device description declares a unique name attribute, for example by adding name="<unique-id>" to each one in the PDSC (device or family debug/trace section). If the duplicates come from a pack you do not control, check which <trace> entries are actually meant to apply to the selected device and processor, since the warning is raised for every matching unnamed buffer.

## Trigger in the source

```cpp
if (traceBufferCount > 1 && unnamedTraceBufferCount > 0) {
```

## Note

The source does not show whether unnamed buffers actually break debug configuration; the message is only a warning and the code still collects the unnamed sink. Pname-tagged trace elements are skipped before counting, so the warning concerns only the non-processor-specific traces. The fix about PDSC naming is inferred from the check, not from a documented rule.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrRunDebug.cpp:575-579`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:582-584`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:592-600`
- `tools/projmgr/src/ProjMgrRunDebug.cpp:607-608`
