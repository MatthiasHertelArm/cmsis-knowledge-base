---
id: "ts-packchk-m345"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M345: URL not found: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M345"
symptoms: ["M345", "URL not found: '%URL%'"]
symptom_regex: "^URL not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The specified URL could not be found."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:163", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:23", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:186"]
---

## Symptom

`M345`
`URL not found: '%URL%'`

## Cause

The specified URL could not be found. Correct the URL. Refer to [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package).

## Fix

Correct the URL named in the message or make the target reachable.

## Note

No raise site for M345 (nor for the progress message M054 'Checking if URL exists') at 30f5e81; packchk does not test URLs there. Fix taken from the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:163`
- `tools/packchk/src/PackChk_Msgs.cpp:23`
- `tools/packchk/README.md:186`
