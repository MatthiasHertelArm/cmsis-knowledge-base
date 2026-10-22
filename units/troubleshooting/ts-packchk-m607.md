---
id: "ts-packchk-m607"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M607: Tag '…' does not allow wildcard specification: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M607"
symptoms: ["M607", "Tag '%TAG%' does not allow wildcard specification: '%NAME%'"]
symptom_regex: "^Tag '.+?' does not allow wildcard specification: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk found a wildcard character in an element of the PDSC file whose tag does not accept wildcards, so the value is taken literally."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M607`
`Tag '%TAG%' does not allow wildcard specification: '%NAME%'`

## Cause

packchk found a wildcard character in an element of the PDSC file whose tag does not accept wildcards, so the value is taken literally. The %TAG% is the PDSC element name and %NAME% is the offending value as written in the pack description.

## Fix

Open the PDSC file at the element named in the message and replace the wildcard pattern with an explicit value, such as one exact name, version or file path. Keep wildcards only in elements that accept them, then rerun packchk.

## Note

The clone was not available, so the trigger and the list of wildcard-capable tags were not checked against the source. The wording of the cause and fix is inferred from the message text alone.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
