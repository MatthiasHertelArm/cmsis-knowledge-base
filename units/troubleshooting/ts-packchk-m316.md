---
id: "ts-packchk-m316"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M316: URL must end with slash '/': '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M316"
symptoms: ["M316", "URL must end with slash '/': '%URL%'"]
symptom_regex: "^URL must end with slash '/': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct package URL _'URL'_. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url)."
summary: "The package description (PDSC) carries a URL in its package URL element whose value does not end with a slash. packchk warns with M316 and echoes the offending value in place of %URL%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; answered from message text and README)"]
---

## Symptom

`M316`
`URL must end with slash '/': '%URL%'`

## Cause

The package description (PDSC) carries a URL in its package URL element whose value does not end with a slash. packchk warns with M316 and echoes the offending value in place of %URL%. Only the message text and the README wording are available here, so the exact element that holds the URL is inferred from the README reference to the package URL.

## Fix

Open the PDSC file named in the build log and make the url value of the package element end with a trailing slash, for example <url>https://example.com/packs/</url>. Re-run packchk to confirm the warning is gone.

## Note

The source lines were not available, so the trigger condition is inferred from the message text and README only. The README wording 'Correct package URL' refers to the package url element of the PDSC, as stated by its link to the package_url section of the spec.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; answered from message text and README)`
