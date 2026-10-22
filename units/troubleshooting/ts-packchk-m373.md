---
id: "ts-packchk-m373"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M373: Unsupported Schema Version: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M373"
symptoms: ["M373", "Unsupported Schema Version: '%VER%'"]
symptom_regex: "^Unsupported Schema Version: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The schema version is not supported. Verify the attribute schemaVersion of the element [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package)."
summary: "packchk found a PDSC whose schemaVersion attribute on the package element names a version it does not support."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M373 Unsupported Schema Version, trigger not inspected)"]
---

## Symptom

`M373`
`Unsupported Schema Version: '%VER%'`

## Cause

packchk found a PDSC whose schemaVersion attribute on the package element names a version it does not support. The %VER% in the message is the schemaVersion value read from the file. Source lines were not available, so this reading comes from the message text and the README.

## Fix

Open the .pdsc file and check the schemaVersion attribute of the root package element. Set it to a schema version supported by the packchk release in use, as described in the CMSIS Pack specification for the package element, then run packchk again.

## Note

Source lines were not available for this entry; the cause and fix rely on the message text and the README. The README points to the package element documentation for the schemaVersion attribute.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M373 Unsupported Schema Version, trigger not inspected)`
