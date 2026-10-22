---
id: "ts-packchk-m205"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M205: Cannot create Pack Name file '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M205"
symptoms: ["M205", "Cannot create Pack Name file '%PATH%'"]
symptom_regex: "^Cannot create Pack Name file '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check the disk space or your permissions. Correct the path name."
summary: "packchk could not create the file named in the message, which is the pack name file it writes while checking the pack."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M205`
`Cannot create Pack Name file '%PATH%'`

## Cause

packchk could not create the file named in the message, which is the pack name file it writes while checking the pack. The most likely reasons are that the target directory is not writable or the disk is full, or that the path itself is invalid. The source lines were not available, so this is taken from the README and the message text only.

## Fix

Check that the directory named in the path exists and is writable by the user running packchk, and that there is enough free disk space. Correct the path if it is malformed, then run packchk again.

## Note

Source lines were unavailable, so the trigger condition is not verified. The cause and fix follow the README text. The %PATH% placeholder is the file path as packchk prints it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
