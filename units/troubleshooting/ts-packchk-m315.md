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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct package URL _'URL'_. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url)."
summary: "The package's url attribute in the PDSC file is set to a value that looks like a Windows drive path (for example C:\\...), which the tool rejects because a package URL must be a web-style location."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)"]
---

## Symptom

`M315`
`Invalid URL / Paths to Drives are not allowed in Package URL: '%URL%'`

## Cause

The package's url attribute in the PDSC file is set to a value that looks like a Windows drive path (for example C:\...), which the tool rejects because a package URL must be a web-style location. The %URL% in the message is the value of that attribute as written in the PDSC.

## Fix

Edit the url attribute of the <package> element in the .pdsc file so it is a valid web URL, for example https://example.com/packs/ ending with a slash, instead of a local drive path. Then run packchk again.

## Note

Derived from the message text and the README only; the source trigger condition was not available to confirm the exact check, so the description of a drive path is inferred from the message wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)`
