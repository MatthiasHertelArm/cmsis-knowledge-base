---
id: "ts-packchk-m108"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M108: Reading PDSC File failed!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M108"
symptoms: ["M108", "Reading PDSC File failed!"]
symptom_regex: "^Reading PDSC File failed!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "XML parsing of the PDSC file failed. Verify syntax of the PDSC file."
summary: "packchk could not parse the PDSC file as XML while reading it, so the pack description was rejected before any checks ran."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M108`
`Reading PDSC File failed!`

## Cause

packchk could not parse the PDSC file as XML while reading it, so the pack description was rejected before any checks ran. The README attributes this to XML syntax errors in the PDSC file; the source lines were not available to confirm the exact trigger.

## Fix

Open the PDSC file named in the surrounding packchk output and check it for XML well-formedness problems such as unclosed or mismatched tags, unescaped & or < characters in text, and a missing or malformed XML declaration. Validate the file with an XML parser or editor, correct the first reported error, and run packchk again.

## Note

The clone was not available, so the trigger was not read from source; the cause and fix come from the message text and the README entry. The 'Needed: fix' flag and the README's advice to verify syntax are consistent with each other.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
