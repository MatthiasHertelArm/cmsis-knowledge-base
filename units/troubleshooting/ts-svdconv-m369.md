---
id: "ts-svdconv-m369"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M369: Enumerated Value '…': <value> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M369"
symptoms: ["M369", "Enumerated Value '%NAME%': <value> not set."]
symptom_regex: "^Enumerated Value '.+?': <value> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <enumeratedValue> has neither a <value> nor <isDefault>true</isDefault>."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:266", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:281", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:282", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:166", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:188"]
---

## Symptom

`M369`
`Enumerated Value '%NAME%': <value> not set.`

## Cause

An <enumeratedValue> has neither a <value> nor <isDefault>true</isDefault>. The enumerated value is dropped.

## Fix

Add the value, for example <value>0x1</value> or <value>#01</value>, or mark the catch-all entry with <isDefault>true</isDefault>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdEnum.cpp:266`
- `tools/svdconv/SVDModel/src/SvdEnum.cpp:281`
- `tools/svdconv/SVDModel/src/SvdEnum.cpp:282`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:166`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:188`
