---
id: "ts-svdconv-m376"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M376: … '…' (<enumeratedValues> '…'): '…' container already defined in …."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M376"
symptoms: ["M376", "%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container already defined in %LINE%."]
symptom_regex: "^.+? '.+?' \\(<enumeratedValues> '.+?'\\): '.+?' container already defined in .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a second enumeratedValues container with the same usage (read, write or read-write) inside one register or field, which the SVD format does not allow."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M376`
`%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container already defined in %LINE%.`

## Cause

svdconv found a second enumeratedValues container with the same usage (read, write or read-write) inside one register or field, which the SVD format does not allow. The %NAME% and %NAME2% placeholders are the register or field and the enumeratedValues name, %USAGE% is the duplicated usage, and %LINE% is the line of the earlier definition.

## Fix

Open the SVD file at the reported location and remove or merge the duplicate enumeratedValues block so that each usage appears at most once per register or field. Then rerun svdconv.

## Note

Source lines were not available, so the cause is inferred from the message text and the trigger description only. The README cause and fix were not provided to me in detail.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
