---
id: "ts-svdconv-m313"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M313: Field '…': LSB > MSB: BitWith calculates to …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M313"
symptoms: ["M313", "Field '%NAME%': LSB > MSB: BitWith calculates to %NUM%"]
symptom_regex: "^Field '.+?': LSB > MSB: BitWith calculates to .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A field's <lsb> is more than one above its <msb> (or a <bitRange> is written with the low bit first), so the computed width msb - lsb + 1 is negative."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:114", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:175", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:176", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:491", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:492", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:132"]
---

## Symptom

`M313`
`Field '%NAME%': LSB > MSB: BitWith calculates to %NUM%`

## Cause

A field's <lsb> is more than one above its <msb> (or a <bitRange> is written with the low bit first), so the computed width msb - lsb + 1 is negative. The field is dropped.

## Fix

Write the most significant bit first: <bitRange>[7:4]</bitRange>, or <lsb>4</lsb><msb>7</msb>.

## Note

If <lsb> is exactly <msb>+1 the width is 0 and M313 is not raised; the header generator then warns with M220. 'BitWith' in the text is a typo.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:114`
- `tools/svdconv/SVDModel/src/SvdField.cpp:175`
- `tools/svdconv/SVDModel/src/SvdField.cpp:176`
- `tools/svdconv/SVDModel/src/SvdField.cpp:491`
- `tools/svdconv/SVDModel/src/SvdField.cpp:492`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:132`
