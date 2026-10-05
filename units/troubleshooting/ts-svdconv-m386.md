---
id: "ts-svdconv-m386"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M386: Name not C compliant: '…' : Brackets [] found"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M386"
symptoms: ["M386", "Name not C compliant: '%NAME%' : Brackets [] found"]
symptom_regex: "^Name not C compliant: '.+?' : Brackets \\[\\] found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A <name> contains square brackets other than a trailing [%s] on a dim element, e.g."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1119-1131", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1180-1184", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:378-386", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:74-93", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/data/nameHasBrackets/SVDTiny.svd:36-52"]
---

## Symptom

`M386`
`Name not C compliant: '%NAME%' : Brackets [] found`

## Cause

A <name> contains square brackets other than a trailing [%s] on a dim element, e.g. <name>Data[0]</name> on a register without <dim>. Brackets are not valid in a C identifier, so svdconv drops the element.

## Fix

Remove the brackets (<name>Data0</name>), or describe the element as an array: <name>Data[%s]</name> with <dim> and <dimIncrement>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1119-1131`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1180-1184`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:378-386`
- `tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:74-93`
- `tools/svdconv/test/data/nameHasBrackets/SVDTiny.svd:36-52`
