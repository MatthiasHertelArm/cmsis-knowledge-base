---
id: "ts-svdconv-m375"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M375: … '…' (<enumeratedValues> '…'): Too many <enumeratedValues> container specified."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M375"
symptoms: ["M375", "%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): Too many <enumeratedValues> container specified."]
symptom_regex: "^.+? '.+?' \\(<enumeratedValues> '.+?'\\): Too many <enumeratedValues> container specified\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A <field> has more than two <enumeratedValues> containers. svdconv allows one container (usage read, write or read-write) or two (one read, one write); the third and later containers are ignored, and M374 follows with the rule."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:531-552", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:193-196"]
---

## Symptom

`M375`
`%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): Too many <enumeratedValues> container specified.`

## Cause

A <field> has more than two <enumeratedValues> containers. svdconv allows one container (usage read, write or read-write) or two (one read, one write); the third and later containers are ignored, and M374 follows with the rule.

## Fix

Merge the extra <enumeratedValues> into the existing ones so the field keeps at most two: one container for all values, or one with <usage>read</usage> and one with <usage>write</usage>.

## Note

CMSIS-SVD.xsd 1.3.9 also limits <enumeratedValues> to maxOccurs=2 in fieldType.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:531-552`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:193-196`
