---
id: "ts-svdconv-m517"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M517: SFD Code generation: Forbidden Trigraph '??…' found in '…'."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M517"
symptoms: ["M517", "SFD Code generation: Forbidden Trigraph '??%CHAR%' found in '%NAME%'."]
symptom_regex: "^SFD Code generation: Forbidden Trigraph '\\?\\?.+?' found in '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "During SFD generation a description contains two question marks followed by another character ('??x'), which a C preprocessor could read as a trigraph. svdconv reports any character after '??', not only the nine trigraph characters, and drops that character."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1268-1274", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:216"]
---

## Symptom

`M517`
`SFD Code generation: Forbidden Trigraph '??%CHAR%' found in '%NAME%'.`

## Cause

During SFD generation a description contains two question marks followed by another character ('??x'), which a C preprocessor could read as a trigraph. svdconv reports any character after '??', not only the nine trigraph characters, and drops that character.

## Fix

Remove or reword the '??' in the <description>, e.g. write a single '?' or '(unknown)'.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1268-1274`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:216`
