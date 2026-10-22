---
id: "ts-packchk-m323"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M323: File/Path not found: '…'. Check correct spelling."
status: "draft"
tool: "packchk"
severity: "error"
code: "M323"
symptoms: ["M323", "File/Path not found: '%PATH%'. Check correct spelling."]
symptom_regex: "^File/Path not found: '.+?'\\. Check correct spelling\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The file or path _'PATH'_ entered in the PDSC file could not be found. Verify the path information."
summary: "packchk checks that the files and paths referenced in the PDSC exist in the pack, and this message is printed when a referenced path %PATH% cannot be found."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text 'File/Path not found' for M323; trigger not visible in the lines provided)"]
---

## Symptom

`M323`
`File/Path not found: '%PATH%'. Check correct spelling.`

## Cause

packchk checks that the files and paths referenced in the PDSC exist in the pack, and this message is printed when a referenced path %PATH% cannot be found. The path most likely comes from a PDSC element such as a file, library or documentation entry that points to a location which is missing or misspelled relative to the pack root. The source lines were not available, so this is taken from the message text and the README cause.

## Fix

Open the PDSC file and locate the element that names the path shown in the message. Check the spelling and letter case of the path and confirm that the file or folder exists at that location relative to the pack root, then rerun packchk.

## Note

Source lines were not available, so the trigger and handling are not verified against code; the cause is inferred from the message text and README. The README and message text agree.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text 'File/Path not found' for M323; trigger not visible in the lines provided)`
