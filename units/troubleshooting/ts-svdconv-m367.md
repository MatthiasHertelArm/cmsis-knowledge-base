---
id: "ts-svdconv-m367"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M367: Access Type: Field '…' (…) does not match Register '…' (…)"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M367"
symptoms: ["M367", "Access Type: Field '%NAME%' (%ACCESS%) does not match Register '%NAME2%' (%ACCESS2%)"]
symptom_regex: "^Access Type: Field '.+?' \\(.+?\\) does not match Register '.+?' \\(.+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A field's effective <access> does not fit its register's effective access: a read-only register may only contain read-only fields, a write-only or writeOnce register only write-only or writeOnce fields, while a read-write register accepts any field access."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:516", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:519", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:520", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1514", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1116", "Open-CMSIS-Pack/devtools@30f5e817:libs/errlog/src/ErrLog.cpp:24", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:186"]
---

## Symptom

`M367`
`Access Type: Field '%NAME%' (%ACCESS%) does not match Register '%NAME2%' (%ACCESS2%)`

## Cause

A field's effective <access> does not fit its register's effective access: a read-only register may only contain read-only fields, a write-only or writeOnce register only write-only or writeOnce fields, while a read-write register accepts any field access. Access not set at any level counts as read-write.

## Fix

Make the field's <access> consistent with the register's: correct the field's <access>, or set the register's <access> to read-write when it holds both readable and writable fields.

## Note

LogMsg("M367", lineNo) passes no names, so the output shows the literal placeholders <NAME>, <ACCESS>, <NAME2>, <ACCESS2>; use the line number to find the field.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:516`
- `tools/svdconv/SVDModel/src/SvdField.cpp:519`
- `tools/svdconv/SVDModel/src/SvdField.cpp:520`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1514`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1116`
- `libs/errlog/src/ErrLog.cpp:24`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:186`
