---
id: "ts-packchk-m327"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M327: Path is not conformant: '…': Backslashes are not recommended, use forward slashes."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M327"
symptoms: ["M327", "Path is not conformant: '%PATH%':   Backslashes are not recommended, use forward slashes."]
symptom_regex: "^Path is not conformant: '.+?':   Backslashes are not recommended, use forward slashes\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Paths to files should adhere to the POSIX standard using forward slashes (/)."
summary: "packchk found a path in the PDSC (for example a file or directory attribute) that contains a backslash, which the tool regards as non-conformant because pack paths are expected to use POSIX forward slashes."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone not available)"]
---

## Symptom

`M327`
`Path is not conformant: '%PATH%':   Backslashes are not recommended, use forward slashes.`

## Cause

packchk found a path in the PDSC (for example a file or directory attribute) that contains a backslash, which the tool regards as non-conformant because pack paths are expected to use POSIX forward slashes. The %PATH% in the message is the offending path as written in the pack description.

## Fix

Open the PDSC file, find the path named in the message, and replace every backslash with a forward slash, for example change Source\Device\file.c to Source/Device/file.c, then rerun packchk.

## Note

Answered from the message text and the README cause only, since the source lines were not available; the exact trigger condition in PackChk_Msgs.cpp was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone not available)`
