---
id: "ts-packchk-m510"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M510: Xerxes reports: …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M510"
symptoms: ["M510", "Xerxes reports: %MSG%"]
symptom_regex: "^Xerxes reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Xerces reported a warning while validating the PDSC against the PACK.xsd schema; %MSG% is the Xerces text and the line is the PDSC line."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:231", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlschemachecker/src/XmlErrorHandler.cpp:22-25", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlschemachecker/src/XmlErrorHandler.cpp:37-46", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlschemachecker/src/XmlValidator.cpp:49-66", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:119-123"]
---

## Symptom

`M510`
`Xerxes reports: %MSG%`

## Cause

Xerces reported a warning while validating the PDSC against the PACK.xsd schema; %MSG% is the Xerces text and the line is the PDSC line.

## Fix

Read the Xerces text and correct the PDSC at that line; make sure the schema in use (--xsd or the installed PACK.xsd) is at least as new as the schemaVersion of the PDSC.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:231`
- `libs/xmlschemachecker/src/XmlErrorHandler.cpp:22-25`
- `libs/xmlschemachecker/src/XmlErrorHandler.cpp:37-46`
- `libs/xmlschemachecker/src/XmlValidator.cpp:49-66`
- `tools/packchk/src/CreateModel.cpp:119-123`
