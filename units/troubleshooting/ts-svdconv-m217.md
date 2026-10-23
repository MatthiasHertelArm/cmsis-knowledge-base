---
id: "ts-svdconv-m217"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M217: Forbidden Trigraph '??…' found in '…'."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M217"
symptoms: ["M217", "Forbidden Trigraph '??%CHAR%' found in '%NAME%'."]
symptom_regex: "^Forbidden Trigraph '\\?\\?.+?' found in '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A <name>, <description> or register <displayName> contains two question marks followed by another character ('??x'), which a C compiler may read as a trigraph once the text lands in the generated header. svdconv flags any character after '??', not …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1155", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1186", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1189", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:217", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:231", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:234", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:84"]
---

## Symptom

`M217`
`Forbidden Trigraph '??%CHAR%' found in '%NAME%'.`

## Cause

A <name>, <description> or register <displayName> contains two question marks followed by another character ('??x'), which a C compiler may read as a trigraph once the text lands in the generated header. svdconv flags any character after '??', not only the nine trigraph characters, and keeps the text unchanged.

## Fix

Rewrite the text so that '??' is never followed by another character, for example use a single '?' or words such as 'unknown'.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1155`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1186`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1189`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:217`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:231`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:234`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:84`
