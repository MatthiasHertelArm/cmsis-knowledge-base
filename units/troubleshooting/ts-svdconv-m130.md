---
id: "ts-svdconv-m130"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M130: Cannot create file '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M130"
symptoms: ["M130", "Cannot create file '%NAME%'"]
symptom_regex: "^Cannot create file '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check user rights."
summary: "svdconv could not create the output file named in the message."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M130`
`Cannot create file '%NAME%'`

## Cause

svdconv could not create the output file named in the message. The README attributes this to missing user rights, which is the usual reason a file cannot be written. The source lines were not available, so the exact trigger is not confirmed here.

## Fix

Check that the user running svdconv has write permission on the output directory and on the target file name, and that the file is not locked or open in another program. Then run the command again, optionally with the output written to a directory the user owns.

## Note

Source lines were not available; cause and fix come from the message text and the README only, so confidence is capped at medium. The README cause is only a permission check; a missing output directory or an invalid file name could also produce this message, which was not verified from source.
