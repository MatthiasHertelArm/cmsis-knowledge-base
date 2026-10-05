---
id: "ts-svdconv-m215"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M215: Size of <dim> is only one element for '…', is this intended?"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M215"
symptoms: ["M215", "Size of <dim> is only one element for '%NAME%', is this intended?"]
symptom_regex: "^Size of <dim> is only one element for '.+?', is this intended\\?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check single element."
summary: "An element has <dim>1</dim>, so the array or list has a single instance."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:182-188", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:82"]
---

## Symptom

`M215`
`Size of <dim> is only one element for '%NAME%', is this intended?`

## Cause

An element has <dim>1</dim>, so the array or list has a single instance.

## Fix

If there is only one instance, remove <dim>, <dimIncrement> and the %s / [%s] placeholder; otherwise set <dim> to the real number of instances.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:182-188`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:82`
