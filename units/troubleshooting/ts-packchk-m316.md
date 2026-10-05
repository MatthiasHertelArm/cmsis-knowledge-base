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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct package URL _'URL'_. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url)."
summary: "The value of the package <url> element does not end with '/'."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:132", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:517-519", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:163"]
---

## Symptom

`M316`
`URL must end with slash '/': '%URL%'`

## Cause

The value of the package <url> element does not end with '/'.

## Fix

Append the slash: <url>https://www.myvendor.com/pack/</url>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:132`
- `tools/packchk/src/ValidateSyntax.cpp:517-519`
- `tools/packchk/README.md:163`
