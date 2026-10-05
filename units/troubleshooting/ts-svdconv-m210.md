---
id: "ts-svdconv-m210"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M210: Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M210"
symptoms: ["M210", "Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section."]
symptom_regex: "^Use new Format CMSIS\\-SVD >= V1\\.1 and add <CPU> Section\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Update schema and add CPU section."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:983-994", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:77"]
---

## Symptom

`M210`
`Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section.`

## Cause

The <device> has schemaVersion="1.0" and no <cpu> element; CMSIS-SVD 1.0 had no <cpu> section.

## Fix

Set schemaVersion on <device> to 1.1 or later (e.g. schemaVersion="1.3") and add a <cpu> element for the core, e.g. <cpu><name>CM4</name><revision>r0p1</revision><endian>little</endian><mpuPresent>true</mpuPresent><fpuPresent>true</fpuPresent><nvicPrioBits>4</nvicPrioBits><vendorSystickConfig>false</vendorSystickConfig></cpu>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:983-994`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:77`
