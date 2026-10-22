---
id: "ts-packchk-m203"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M203: Error reading PDSC file(s) '…'!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M203"
symptoms: ["M203", "Error reading PDSC file(s) '%PATH%'!"]
symptom_regex: "^Error reading PDSC file\\(s\\) '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Verify the PDSC file for consistency."
summary: "packchk could not read or parse the PDSC file named in the message (the %PATH% part)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M203`
`Error reading PDSC file(s) '%PATH%'!`

## Cause

packchk could not read or parse the PDSC file named in the message (the %PATH% part). The README only says to verify the PDSC file for consistency. The source lines were not available, so the exact parse step that failed is not confirmed.

## Fix

Open the PDSC file named in the message and check that it is well-formed XML (matching tags, valid characters, a single root element) and that it is readable at that path. Then run packchk again on the pack.

## Note

Source lines were unavailable, so the trigger condition is inferred from the message text and the README rather than read from the code. The README wording is vague; a reviewer should confirm the failure modes against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
