---
id: "ts-packchk-m311"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M311: Redefinition of '…' : '…', see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M311"
symptoms: ["M311", "Redefinition of '%TAG%' : '%NAME%', see Line %LINE%"]
symptom_regex: "^Redefinition of '.+?' : '.+?', see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove the redefinition of element _'TAG'_ with name _'NAME'_."
summary: "Two <memory> elements that apply to the same device and processor (including memories inherited from family and subFamily) have the same name, or the same id when name is absent."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:127", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:212-278", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:160"]
---

## Symptom

`M311`
`Redefinition of '%TAG%' : '%NAME%', see Line %LINE%`

## Cause

Two <memory> elements that apply to the same device and processor (including memories inherited from family and subFamily) have the same name, or the same id when name is absent.

## Fix

Give each memory region a unique name (or id), or remove the duplicate definition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:127`
- `tools/packchk/src/ValidateSemantic.cpp:212-278`
- `tools/packchk/README.md:160`
