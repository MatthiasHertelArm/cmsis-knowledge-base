---
id: "ts-svdconv-m201"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M201: Tag <…> unknown or not allowed on this level."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M201"
symptoms: ["M201", "Tag <%TAG%> unknown or not allowed on this level."]
symptom_regex: "^Tag <.+?> unknown or not allowed on this level\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check tag"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:236-262", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:134-136", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:68"]
---

## Symptom

`M201`
`Tag <%TAG%> unknown or not allowed on this level.`

## Cause

An element is misspelled or placed under a parent that does not accept it, e.g. <headerStructName> inside a <register>, or <protection> inside a <field> or <interrupt>. svdconv ignores the element; only the first 10 unknown tags of a run are reported.

## Fix

Check the tag spelling (names are case-sensitive) and move the element to a level where CMSIS-SVD.xsd allows it, or delete it. Vendor-specific data belongs in <vendorExtensions> at the end of <device>.

## Note

The 10-message limit is a static counter (SvdItem.cpp:210, 260); misplaced <protection> is always reported. Tags containing 'dim' are routed to the dim check and give M240 instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:236-262`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:134-136`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:68`
