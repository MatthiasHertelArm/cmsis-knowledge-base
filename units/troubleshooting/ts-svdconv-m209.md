---
id: "ts-svdconv-m209"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M209: CPU section not set. This is required for CMSIS Headerfile generation and debug support."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M209"
symptoms: ["M209", "CPU section not set. This is required for CMSIS Headerfile generation and debug support."]
symptom_regex: "^CPU section not set\\. This is required for CMSIS Headerfile generation and debug support\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add CPU section."
summary: "The <device> has no <cpu> element. svdconv needs it for the core configuration in the CMSIS header and for the interrupt checks, and debuggers use it; header generation reports M209 again."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:983-994", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData.cpp:116-119", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:309-335", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:76"]
---

## Symptom

`M209`
`CPU section not set. This is required for CMSIS Headerfile generation and debug support.`

## Cause

The <device> has no <cpu> element. svdconv needs it for the core configuration in the CMSIS header and for the interrupt checks, and debuggers use it; header generation reports M209 again.

## Fix

Add a <cpu> element to <device> (after <description>/<licenseText>) with the values of the actual core, e.g. <cpu><name>CM4</name><revision>r0p1</revision><endian>little</endian><mpuPresent>true</mpuPresent><fpuPresent>true</fpuPresent><nvicPrioBits>4</nvicPrioBits><vendorSystickConfig>false</vendorSystickConfig></cpu>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:983-994`
- `tools/svdconv/SVDGenerator/src/HeaderData.cpp:116-119`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:309-335`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:76`
