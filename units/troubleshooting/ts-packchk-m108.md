---
id: "ts-packchk-m108"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M108: Reading PDSC File failed!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M108"
symptoms: ["M108", "Reading PDSC File failed!"]
symptom_regex: "^Reading PDSC File failed!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "XML parsing of the PDSC file failed."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:79", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:119-130", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk.cpp:117-120", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmltreeslim/src/XmlTreeSlimInterface.cpp:104-133", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlreader/src/XML_Reader.cpp:740-790", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:120"]
---

## Symptom

`M108`
`Reading PDSC File failed!`

## Cause

XML parsing of the PDSC file failed. Verify syntax of the PDSC file.

## Fix

Fix the XML syntax errors that the XML reader reports just before M108 with line numbers (for example a missing end tag, or a bare '&' or '<' in text that must be written &amp; or &lt;), then run packchk again; until the PDSC parses, the later checks have no model to work on.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:79`
- `tools/packchk/src/RteModelReader.cpp:119-130`
- `tools/packchk/src/PackChk.cpp:117-120`
- `libs/xmltreeslim/src/XmlTreeSlimInterface.cpp:104-133`
- `libs/xmlreader/src/XML_Reader.cpp:740-790`
- `tools/packchk/README.md:120`
