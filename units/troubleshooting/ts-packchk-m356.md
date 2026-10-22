---
id: "ts-packchk-m356"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M356: Path '…' does not specify a file!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M356"
symptoms: ["M356", "Path '%PATH%' does not specify a file!"]
symptom_regex: "^Path '.+?' does not specify a file!$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk reports this when a path given in the PDSC is a directory, or a path without a file name, where a file reference is required."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M356`
`Path '%PATH%' does not specify a file!`

## Cause

packchk reports this when a path given in the PDSC is a directory, or a path without a file name, where a file reference is required. The %PATH% placeholder is the offending path as written in the pack description. Without the source lines the exact check cannot be confirmed here.

## Fix

Open the PDSC entry named in the message and make the referenced path point to a concrete file (for example a header, source, or documentation file) rather than a folder or an empty value, then rerun packchk.

## Note

Trigger inferred from the message text only; the clone was not available, so the exact condition in the source is unverified. Not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
