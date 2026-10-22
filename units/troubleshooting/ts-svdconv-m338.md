---
id: "ts-svdconv-m338"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M338: Field '…' … (…) overlaps '…' … (…) …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M338"
symptoms: ["M338", "Field '%NAME%' %BITRANGE% (%ACCESS%) overlaps '%NAME2%' %BITRANGE2% (%ACCESS2%) %LINE%"]
symptom_regex: "^Field '.+?' .+? \\(.+?\\) overlaps '.+?' .+? \\(.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two fields inside the same register in the SVD file occupy overlapping bit ranges, and at least one of them is writable or the overlap is otherwise not allowed by svdconv's field check."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M338`
`Field '%NAME%' %BITRANGE% (%ACCESS%) overlaps '%NAME2%' %BITRANGE2% (%ACCESS2%) %LINE%`

## Cause

Two fields inside the same register in the SVD file occupy overlapping bit ranges, and at least one of them is writable or the overlap is otherwise not allowed by svdconv's field check. The message names the two fields, their bit ranges and access types, and the line where the second one appears. The overlap is in the SVD register description, not in the csolution project.

## Fix

Open the SVD file at the line reported and correct the offending <field> entries so that their <bitOffset>/<bitWidth> (or <lsb>/<msb>) ranges do not intersect within that register. If the overlap is intentional, for example a read-only alias over a writable field, the field access types or the register definition need to reflect that; check the vendor's register documentation to decide which field is correct. Then rerun svdconv on the corrected SVD.

## Note

Source lines were not available, so the trigger condition and the exact access-type rule behind the message are inferred from the message text and the README, not confirmed in code. The exact fix depends on whether the overlap is an SVD authoring error or a deliberate alias.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
