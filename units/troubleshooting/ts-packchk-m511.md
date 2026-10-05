---
id: "ts-packchk-m511"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M511: Xerxes reports: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M511"
symptoms: ["M511", "Xerxes reports: %MSG%"]
symptom_regex: "^Xerxes reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The PDSC does not validate against PACK.xsd: Xerces reports an element or attribute the schema does not allow at that place, a missing required attribute, a value that breaks the schema type or pattern, or XML that is not well-formed."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:232", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlschemachecker/src/XmlErrorHandler.cpp:17-30", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlschemachecker/src/XmlValidator.cpp:49-79", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:119-123", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:952-986"]
---

## Symptom

`M511`
`Xerxes reports: %MSG%`

## Cause

The PDSC does not validate against PACK.xsd: Xerces reports an element or attribute the schema does not allow at that place, a missing required attribute, a value that breaks the schema type or pattern, or XML that is not well-formed. It is also printed as 'Exception: ...' when the schema or PDSC cannot be read. packchk continues with its other checks.

## Fix

Correct the PDSC at the reported line as the Xerces text says (element spelling and order, allowed attribute values, required attributes). If the element is valid in a newer pack schema, point --xsd at a PACK.xsd of that version.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:232`
- `libs/xmlschemachecker/src/XmlErrorHandler.cpp:17-30`
- `libs/xmlschemachecker/src/XmlValidator.cpp:49-79`
- `tools/packchk/src/CreateModel.cpp:119-123`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:952-986`
