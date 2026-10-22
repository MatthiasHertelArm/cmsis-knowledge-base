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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Set a valid schema version in the PDSC file. Refer to schemaVersion attribute in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package)."
summary: "packchk found no schemaVersion attribute on the root package element of the PDSC file, so it reports that the schema version is not set."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M376`
`Schema Version not set!`

## Cause

packchk found no schemaVersion attribute on the root package element of the PDSC file, so it reports that the schema version is not set. The message is printed from the PDSC check, and the README attributes it to a missing or invalid schemaVersion on the package element.

## Fix

Open the PDSC file and set a valid schemaVersion attribute on the root <package> element, as described in the CMSIS Pack specification for the package element, then run packchk again.

## Note

Source lines were not available, so the trigger condition is taken from the message text and the README only. The README says 'valid' schema version, which may also cover a schemaVersion value the tool does not accept; this could not be verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
