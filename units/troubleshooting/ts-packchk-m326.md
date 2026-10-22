---
id: "ts-packchk-m326"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M326: Path is not conformant: '…': Absolute Paths or Drive references are not allowed, use Paths relative …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M326"
symptoms: ["M326", "Path is not conformant: '%PATH%':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file."]
symptom_regex: "^Path is not conformant: '.+?':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The path needs to be relative to the PDSC file so that a dependency of a certain file system does not occur."
summary: "packchk found a path in the PDSC that is absolute or starts with a drive letter, such as an absolute file system location or a Windows drive reference."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M326`
`Path is not conformant: '%PATH%':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file.`

## Cause

packchk found a path in the PDSC that is absolute or starts with a drive letter, such as an absolute file system location or a Windows drive reference. Pack paths must be relative to the PDSC file so the pack stays portable across file systems. The '%PATH%' in the message is the offending path string as written in the PDSC. This is inferred from the message text and the README, since the source lines were not available.

## Fix

Open the PDSC file, find the path named in the message and change it to a path relative to the directory that contains the PDSC file, for example replace an absolute location or a drive-letter path with a relative one such as ./Source/file.c, then run packchk again.

## Note

Source lines were not provided, so the trigger condition is not verified from code; the cause and fix rely on the message text and the README. The evidence entry names only the file given in the message header.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
