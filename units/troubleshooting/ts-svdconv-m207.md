---
id: "ts-svdconv-m207"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M207: Expression marker found but no <dim> specified: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M207"
symptoms: ["M207", "Expression marker found but no <dim> specified: '%NAME%'"]
symptom_regex: "^Expression marker found but no <dim> specified: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Specify dimension."
summary: "An element without <dim> has %s or a trailing [%s] in its <name>, <displayName> or <description>."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1288-1311", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:125-200", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:74"]
---

## Symptom

`M207`
`Expression marker found but no <dim> specified: '%NAME%'`

## Cause

An element without <dim> has %s or a trailing [%s] in its <name>, <displayName> or <description>. These placeholders are expanded only for dim elements, so svdconv drops the element; a literal '%s' in a description triggers it too. NAME shows the text with the placeholder removed.

## Fix

Add <dim> and <dimIncrement> (and <dimIndex> for a %s list) if the element is meant to repeat; otherwise remove %s / [%s] from the name, displayName and description.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:1288-1311`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:125-200`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:74`
