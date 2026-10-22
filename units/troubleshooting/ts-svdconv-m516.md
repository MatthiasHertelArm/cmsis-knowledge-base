---
id: "ts-svdconv-m516"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M516: SFD Code generation: Unsupported character found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M516"
symptoms: ["M516", "SFD Code generation: Unsupported character found in '%NAME%' : %HEX%."]
symptom_regex: "^SFD Code generation: Unsupported character found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "During SFD generation (--generate=sfd or sfr) a text contains a character svdconv cannot write into the SFD file: a byte outside printable ASCII 0x20..0x7E (UTF-8 letters, µ, ©, typographic quotes or dashes, each byte reported separately) or a double quote."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1238-1300", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:78", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:262", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:874", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:1044", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:217"]
---

## Symptom

`M516`
`SFD Code generation: Unsupported character found in '%NAME%' : %HEX%.`

## Cause

During SFD generation (--generate=sfd or sfr) a text contains a character svdconv cannot write into the SFD file: a byte outside printable ASCII 0x20..0x7E (UTF-8 letters, µ, ©, typographic quotes or dashes, each byte reported separately) or a double quote. The description of a peripheral, cluster, register, field, interrupt or enumerated value is checked, falling back to its displayName or name; non-ASCII bytes are dropped and double quotes escaped.

## Fix

Replace the character in the <description> (or <displayName>/<name> when there is no description) with plain ASCII, e.g. 'u' or 'micro' for µ, ' instead of typographic quotes, - instead of an en dash, and avoid double quotes.

## Note

Called without a line number (default -1). The same text usually raised M216 in the check phase.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1238-1300`
- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:78`
- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:262`
- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:874`
- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:1044`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:217`
