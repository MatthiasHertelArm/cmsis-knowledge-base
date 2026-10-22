---
id: "ts-svdconv-m308"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M308: Number of <dimIndex> Elements '…' is different to number of <dim> instances '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M308"
symptoms: ["M308", "Number of <dimIndex> Elements '%NUM%' is different to number of <dim> instances '%NUM2%'"]
symptom_regex: "^Number of <dimIndex> Elements '.+?' is different to number of <dim> instances '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file declares a register or peripheral array (a <dim> element) whose <dimIndex> list does not have the same number of entries as the <dim> count. svdconv reports both numbers: the count of <dimIndex> elements and the value …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M308 definition; trigger lines not available in this session)"]
---

## Symptom

`M308`
`Number of <dimIndex> Elements '%NUM%' is different to number of <dim> instances '%NUM2%'`

## Cause

The SVD file declares a register or peripheral array (a <dim> element) whose <dimIndex> list does not have the same number of entries as the <dim> count. svdconv reports both numbers: the count of <dimIndex> elements and the value of <dim>. The mismatch is in the SVD input, not in the svdconv command line.

## Fix

Open the SVD file at the element named in the message and make the <dimIndex> entries match the <dim> value: either list exactly <dim> indices (for example 0..N-1 or the explicit names) or correct the <dim> count so it equals the number of indices. Then rerun svdconv.

## Note

Cause and fix derived from the message text and the README entry; the source trigger lines could not be inspected, so the exact comparison and any exception path are unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M308 definition; trigger lines not available in this session)`
