---
id: "ts-packchk-m309"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M309: Attribute '…' missing on '…' (when '…' is specified)"
status: "draft"
tool: "packchk"
severity: "error"
code: "M309"
symptoms: ["M309", "Attribute '%TAG%' missing on '%TAG2%' (when '%TAG3%' is specified)"]
symptom_regex: "^Attribute '.+?' missing on '.+?' \\(when '.+?' is specified\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add missing attribute _'TAG'_ or remove the attribute _'TAG3'_ in the element _'TAG2'_."
summary: "packchk reports this when an element of a PDSC file carries an attribute that requires a companion attribute which is absent."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M309`
`Attribute '%TAG%' missing on '%TAG2%' (when '%TAG3%' is specified)`

## Cause

packchk reports this when an element of a PDSC file carries an attribute that requires a companion attribute which is absent. The message names the missing attribute (%TAG%), the element that lacks it (%TAG2%) and the attribute whose presence triggers the requirement (%TAG3%). The source lines were not available, so this is based on the message text and the README only.

## Fix

Open the PDSC element named in the message and either add the missing attribute named in the message with a valid value, or remove the attribute that triggered the requirement, then re-run packchk.

## Note

Trigger not verified in source; the clone was unavailable, so the cause and fix rest on the message text and the README wording. The README's 'TAG' and 'TAG3' placeholders match the message variables, so the mapping is consistent.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
