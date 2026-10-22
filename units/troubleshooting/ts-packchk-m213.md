---
id: "ts-packchk-m213"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M213: Found blank char '…' in Packname output filename, deleted"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M213"
symptoms: ["M213", "Found blank char '%NUM%' in Packname output filename, deleted"]
symptom_regex: "^Found blank char '.+?' in Packname output filename, deleted$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk found a blank (whitespace) character in the pack name used to build the output filename, and removed it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M213`
`Found blank char '%NUM%' in Packname output filename, deleted`

## Cause

packchk found a blank (whitespace) character in the pack name used to build the output filename, and removed it. The %NUM% in the message is the character code of the blank that was found. This is a warning, the pack is still produced, but the filename no longer matches the name written in the PDSC.

## Fix

Remove spaces and other blank characters from the pack name, for example the name in the PDSC <name> element or the name given to the packaging step, so that the generated filename contains no blanks. Then run packchk again and confirm the M213 warning is gone.

## Note

The clone was not available, so this entry is written from the message text alone and the cause and fix are inferred, not read from the trigger code. Verify the exact input field against the source before relying on it. The fix assumes the blank comes from the pack name and not from another input.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
