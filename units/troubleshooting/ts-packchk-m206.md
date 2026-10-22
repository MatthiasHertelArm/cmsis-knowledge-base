---
id: "ts-packchk-m206"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M206: Multiple PDSC file found in package: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M206"
symptoms: ["M206", "Multiple PDSC file found in package: %FILES%"]
symptom_regex: "^Multiple PDSC file found in package: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Only one PDSC file is allowed in a package. Remove unnecessary PDSC files. The message lists all \\*.pdsc files found."
summary: "packchk found more than one *.pdsc file in the package directory it checks, and the message lists them in %FILES%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M206`
`Multiple PDSC file found in package: %FILES%`

## Cause

packchk found more than one *.pdsc file in the package directory it checks, and the message lists them in %FILES%. A CMSIS pack is expected to carry exactly one PDSC description file, so the extra files make the package ambiguous.

## Fix

Remove or move the extra *.pdsc files out of the package directory so that only the intended PDSC file remains, then rerun packchk. Check the listed file names in the message to find which ones to remove.

## Note

Source lines were not available; the cause and fix are taken from the message text and the README, not verified against the trigger code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
