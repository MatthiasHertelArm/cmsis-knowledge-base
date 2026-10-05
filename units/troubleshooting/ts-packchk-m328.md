---
id: "ts-packchk-m328"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M328: Version not set for Release Information '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M328"
symptoms: ["M328", "Version not set for Release Information '%DESCR%'"]
symptom_regex: "^Version not set for Release Information '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The release defined through the description _'DESCR'_ requires the attribute `<version>`."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:144", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:303-310", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:169"]
---

## Symptom

`M328`
`Version not set for Release Information '%DESCR%'`

## Cause

The release defined through the description _'DESCR'_ requires the attribute `<version>`. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

Add the version attribute to the <release>, e.g. <release version="1.2.0" date="2026-01-31">...</release>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:144`
- `tools/packchk/src/ValidateSyntax.cpp:303-310`
- `tools/packchk/README.md:169`
