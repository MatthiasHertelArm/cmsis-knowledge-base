---
id: "ts-packchk-m311"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M311: Redefinition of '…' : '…', see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M311"
symptoms: ["M311", "Redefinition of '%TAG%' : '%NAME%', see Line %LINE%"]
symptom_regex: "^Redefinition of '.+?' : '.+?', see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove the redefinition of element _'TAG'_ with name _'NAME'_."
summary: "packchk prints this when the same PDSC element, identified by its tag and name, is declared more than once. %TAG% is the element tag and %NAME% the duplicated name, and %LINE% points to the earlier declaration that the second …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; trigger lines not available)"]
---

## Symptom

`M311`
`Redefinition of '%TAG%' : '%NAME%', see Line %LINE%`

## Cause

packchk prints this when the same PDSC element, identified by its tag and name, is declared more than once. %TAG% is the element tag and %NAME% the duplicated name, and %LINE% points to the earlier declaration that the second one clashes with. The source lines are not available, so this is inferred from the message text and the README rather than from the trigger code.

## Fix

Open the PDSC file at the line given in the message and delete or rename the duplicate element so that each element tag and name pair appears only once, then rerun packchk.

## Note

Cause and fix are taken from the README text and the message wording; the trigger condition in the source was not checked, so the exact comparison used to detect the redefinition is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; trigger lines not available)`
