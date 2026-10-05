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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:192", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:386-399", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:211"]
---

## Symptom

`M373`
`Unsupported Schema Version: '%VER%'`

## Cause

The schema version is not supported. Verify the attribute schemaVersion of the element [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package).

## Fix

Set schemaVersion on <package> to a version of the pack schema the tools support, e.g. schemaVersion="1.7.15", and validate against the matching PACK.xsd.

## Note

No raise site for M373 at 30f5e81; packchk only checks that schemaVersion is present (M376). Fix inferred from the message and README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:192`
- `tools/packchk/src/ValidateSyntax.cpp:386-399`
- `tools/packchk/README.md:211`
