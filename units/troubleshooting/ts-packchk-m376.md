---
id: "ts-packchk-m376"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M376: Schema Version not set!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M376"
symptoms: ["M376", "Schema Version not set!"]
symptom_regex: "^Schema Version not set!$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Set a valid schema version in the PDSC file. Refer to schemaVersion attribute in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package)."
summary: "The <package> element has no schemaVersion attribute."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:195", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:386-399", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:214"]
---

## Symptom

`M376`
`Schema Version not set!`

## Cause

The <package> element has no schemaVersion attribute.

## Fix

Add schemaVersion to <package>, e.g. <package schemaVersion="1.7.15" ...>, naming the pack schema version the PDSC is written for.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:195`
- `tools/packchk/src/ValidateSyntax.cpp:386-399`
- `tools/packchk/README.md:214`
