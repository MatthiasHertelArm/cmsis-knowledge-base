---
id: "ts-packchk-m315"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M315: Invalid URL / Paths to Drives are not allowed in Package URL: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M315"
symptoms: ["M315", "Invalid URL / Paths to Drives are not allowed in Package URL: '%URL%'"]
symptom_regex: "^Invalid URL / Paths to Drives are not allowed in Package URL: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct package URL _'URL'_. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url)."
summary: "The <url> of the package has ':' as its second character, i.e. it starts with a drive letter such as \"C:/packs/\" instead of a web address."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:131", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:513-515", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:162"]
---

## Symptom

`M315`
`Invalid URL / Paths to Drives are not allowed in Package URL: '%URL%'`

## Cause

The <url> of the package has ':' as its second character, i.e. it starts with a drive letter such as "C:/packs/" instead of a web address.

## Fix

Set <url> to the web location the pack is downloaded from, e.g. <url>https://www.myvendor.com/pack/</url>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:131`
- `tools/packchk/src/ValidateSyntax.cpp:513-515`
- `tools/packchk/README.md:162`
