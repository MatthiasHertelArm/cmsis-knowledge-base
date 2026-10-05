---
id: "ts-svdconv-m333"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M333: Duplicate <enumeratedValue> …: '…' (…), already used by '…' (…) …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M333"
symptoms: ["M333", "Duplicate <enumeratedValue> %NUM%: '%NAME%' (%USAGE%), already used by '%NAME2%' (%USAGE2%) %LINE%"]
symptom_regex: "^Duplicate <enumeratedValue> .+?: '.+?' \\(.+?\\), already used by '.+?' \\(.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:374", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:400", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:403", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:627", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:152", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:240"]
---

## Symptom

`M333`
`Duplicate <enumeratedValue> %NUM%: '%NAME%' (%USAGE%), already used by '%NAME2%' (%USAGE2%) %LINE%`

## Cause

Two <enumeratedValue>s in the same <enumeratedValues> container of a field have the same <value>; USAGE shows the container's usage. The later one is dropped. Warning by default, error with --strict.

## Fix

Give each enumeratedValue in a container a distinct <value>, or delete the duplicate. If a value means something different on read and on write, use two containers, one with <usage>read</usage> and one with <usage>write</usage>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:374`
- `tools/svdconv/SVDModel/src/SvdField.cpp:400`
- `tools/svdconv/SVDModel/src/SvdField.cpp:403`
- `tools/svdconv/SVDModel/src/SvdField.cpp:627`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:152`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:240`
