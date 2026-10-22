---
id: "ts-packchk-m313"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M313: Associated File/Path is outside PACK root: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M313"
symptoms: ["M313", "Associated File/Path is outside PACK root: '%PATH%'"]
symptom_regex: "^Associated File/Path is outside PACK root: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk found a file or path referenced from the PDSC (for example a file element or an associated file) that resolves to a location outside the pack root directory."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in this session; message text only)"]
---

## Symptom

`M313`
`Associated File/Path is outside PACK root: '%PATH%'`

## Cause

packchk found a file or path referenced from the PDSC (for example a file element or an associated file) that resolves to a location outside the pack root directory. The '%PATH%' in the message is the offending path as written or resolved. Packs must keep all their content under the pack root, so such a reference cannot be packaged.

## Fix

Edit the PDSC so the referenced path is relative to the pack root and points to a file inside it (for example move the file into the pack directory and reference it with a relative path that does not climb above the root with '..'). Then rerun packchk.

## Note

Source lines were not available, so the trigger condition and the exact path resolution are inferred from the message text only; the fix is the general remedy and should be checked against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in this session; message text only)`
