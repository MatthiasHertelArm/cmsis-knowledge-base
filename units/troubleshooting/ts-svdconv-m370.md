---
id: "ts-svdconv-m370"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M370: … '…': <offset> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M370"
symptoms: ["M370", "%LEVEL% '%NAME%': <offset> not set."]
symptom_regex: "^.+? '.+?': <offset> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv reports that a register-hierarchy element (such as a peripheral, cluster, or register named by %NAME%) in the SVD input has no address offset set, so it cannot compute where that element sits in the address map."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; trigger lines not available)"]
---

## Symptom

`M370`
`%LEVEL% '%NAME%': <offset> not set.`

## Cause

svdconv reports that a register-hierarchy element (such as a peripheral, cluster, or register named by %NAME%) in the SVD input has no address offset set, so it cannot compute where that element sits in the address map. The %LEVEL% placeholder identifies which kind of element is missing the value. The source lines were not available, so this is inferred from the message text alone.

## Fix

Open the SVD file and find the element named in the message. Add or correct its <addressOffset> (or the peripheral's <baseAddress>, for a peripheral) so every register, cluster and peripheral has a numeric offset, then re-run svdconv.

## Note

Source lines were not available, so the trigger condition and which element kinds the check covers are not verified. The fix refers to the usual SVD elements for offsets and should be checked against the README text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; trigger lines not available)`
