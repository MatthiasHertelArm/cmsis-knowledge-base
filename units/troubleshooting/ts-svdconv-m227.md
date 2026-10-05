---
id: "ts-svdconv-m227"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M227: SFD Code generation warning: …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M227"
symptoms: ["M227", "SFD Code generation warning: %MSG%"]
symptom_regex: "^SFD Code generation warning: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A field wider than 6 bits has <enumeratedValues> with values."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:954", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:962", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdUtils.h:31", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:382", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:94"]
---

## Symptom

`M227`
`SFD Code generation warning: %MSG%`

## Cause

A field wider than 6 bits has <enumeratedValues> with values. The System Viewer (SFD) file builds a drop-down list of values only for fields of up to 6 bits, so the list for this field is left out; MSG names the field and its width.

## Fix

Nothing in the SVD must change; the field itself is still generated. If the warning should go away, remove the <enumeratedValues> from fields wider than 6 bits, or correct the field's bit range if it is really 6 bits or narrower.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:954`
- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:962`
- `tools/svdconv/SVDModel/include/SvdUtils.h:31`
- `tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:382`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:94`
