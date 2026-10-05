---
id: "ts-svdconv-m203"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M203: Value already set: <…> = '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M203"
symptoms: ["M203", "Value already set: <%TAG%> = '%VALUE%'"]
symptom_regex: "^Value already set: <.+?> = '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check tag/value."
summary: "In this svdconv version it is raised only for the derivedFrom attribute: an element receives a derivedFrom reference while it already has one."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:267-285", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:178-182", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmltree/include/XmlItem.h:119", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:70"]
---

## Symptom

`M203`
`Value already set: <%TAG%> = '%VALUE%'`

## Cause

In this svdconv version it is raised only for the derivedFrom attribute: an element receives a derivedFrom reference while it already has one. An XML element cannot carry the attribute twice, so a well-formed SVD file should not produce it.

## Fix

Keep a single derivedFrom attribute on the element at the reported line; if the message persists, report it with the SVD file to Open-CMSIS-Pack/devtools.

## Note

Attributes are stored in a std::map and processed once per element, so the condition looks unreachable from a file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:267-285`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:178-182`
- `libs/xmltree/include/XmlItem.h:119`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:70`
