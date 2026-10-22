---
id: "ts-packchk-m308"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M308: Attribute '…' missing on '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M308"
symptoms: ["M308", "Attribute '%TAG%' missing on '%TAG2%'"]
symptom_regex: "^Attribute '.+?' missing on '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Element _'TAG2'_ requires attribute _'TAG'_, but it was not found. Add missing attribute."
summary: "packchk prints this when a required XML attribute (the variable %TAG%) is absent from an element (the variable %TAG2%) of the pack description, most likely the PDSC file."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M308`
`Attribute '%TAG%' missing on '%TAG2%'`

## Cause

packchk prints this when a required XML attribute (the variable %TAG%) is absent from an element (the variable %TAG2%) of the pack description, most likely the PDSC file. The README attributes it to a required attribute that was not found on the element. The source lines were not available, so the exact element and attribute cannot be confirmed from code.

## Fix

Open the PDSC element named in the message, compare it with the schema for that element, and add the missing attribute with a valid value, then rerun packchk.

## Note

Source lines were unavailable; cause is inferred from the message text and the README entry only. The README says 'Add missing attribute' without naming the attribute, so the user must read it from the message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
