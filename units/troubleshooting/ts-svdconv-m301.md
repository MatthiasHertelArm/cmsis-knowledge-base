---
id: "ts-svdconv-m301"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M301: Interrupt number '… : …' already defined: … …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M301"
symptoms: ["M301", "Interrupt number '%NUM% : %NAME%' already defined: %NAME2% %LINE%"]
symptom_regex: "^Interrupt number '.+? : .+?' already defined: .+? .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:186", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:207", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:213", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:216", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:120"]
---

## Symptom

`M301`
`Interrupt number '%NUM% : %NAME%' already defined: %NAME2% %LINE%`

## Cause

Two <interrupt> elements have the same <value> (interrupt number) but different <name>s; interrupt numbers are unique across the whole device. The first definition (at LINE) is kept and the second is not used.

## Fix

Give each interrupt its correct <value>. If two peripherals really share one interrupt line, use the same <name> and <value> in both, which svdconv accepts (it only notes this with the low-level warning M304).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:186`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:207`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:213`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:216`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:120`
