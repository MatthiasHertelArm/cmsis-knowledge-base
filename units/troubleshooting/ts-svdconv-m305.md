---
id: "ts-svdconv-m305"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M305: Name not C compliant: '…' : …, replaced by '_'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M305"
symptoms: ["M305", "Name not C compliant: '%NAME%' : %HEX%, replaced by '_'"]
symptom_regex: "^Name not C compliant: '.+?' : .+?, replaced by '_'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A <name> contains a character that is not allowed in a C identifier: space, backslash, ':', ';', '.', ',', '#', '?', '(', ')', '+', '-', '*' or '/'. svdconv replaces each such character with '_' (one message per character) …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1099", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1105", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1111", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:217", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:222", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:227", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:124"]
---

## Symptom

`M305`
`Name not C compliant: '%NAME%' : %HEX%, replaced by '_'`

## Cause

A <name> contains a character that is not allowed in a C identifier: space, backslash, ':', ';', '.', ',', '#', '?', '(', ')', '+', '-', '*' or '/'. svdconv replaces each such character with '_' (one message per character) and continues with the changed name; names of <enumeratedValue>s are not checked this way.

## Fix

Use only letters, digits and '_' in <name> (the dim placeholder %s is fine), and put human-readable text into <description> or, for registers, <displayName>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1099`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1105`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1111`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:217`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:222`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:227`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:124`
