---
id: "ts-packchk-m103"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M103: Internal Error: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M103"
symptoms: ["M103", "Internal Error: %REF%"]
symptom_regex: "^Internal Error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Contact Arm for clarifications"
summary: "During the letter-case check of a file path from the PDSC, packchk could not find one path segment in the folder listing although the file exists; the text reads 'Internal Error: file/folder \"<segment>\" not found'."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:74", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:511-550", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:461-474", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:143-156", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:118"]
---

## Symptom

`M103`
`Internal Error: %REF%`

## Cause

During the letter-case check of a file path from the PDSC, packchk could not find one path segment in the folder listing although the file exists; the text reads 'Internal Error: file/folder "<segment>" not found'. A doubled slash such as "Files//test.c" produces an empty segment and triggers it.

## Fix

Look at the segment named in the message and fix the path in the PDSC: remove doubled or stray slashes and make every folder and file name match the name on disk.

## Note

Only raise site is CheckFiles::CheckCaseSense; the README advice 'Contact Arm' does not explain it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:74`
- `tools/packchk/src/CheckFiles.cpp:511-550`
- `tools/packchk/src/CheckFiles.cpp:461-474`
- `libs/rteutils/src/RteUtils.cpp:143-156`
- `tools/packchk/README.md:118`
