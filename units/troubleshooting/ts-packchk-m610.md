---
id: "ts-packchk-m610"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M610: File category '…': '…' redefined in component '…', see Line …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M610"
symptoms: ["M610", "File category '%CAT%': '%NAME%' redefined in component '%NAME2%', see Line %LINE%"]
symptom_regex: "^File category '.+?': '.+?' redefined in component '.+?', see Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk found the same file category and name defined more than once across the component definitions of the pack, so a later component redefines an entry already given by an earlier one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available; message text only)"]
---

## Symptom

`M610`
`File category '%CAT%': '%NAME%' redefined in component '%NAME2%', see Line %LINE%`

## Cause

packchk found the same file category and name defined more than once across the component definitions of the pack, so a later component redefines an entry already given by an earlier one. The %CAT% and %NAME% fields show the file category and file name, %NAME2% the component that redefines it, and %LINE% the line of the earlier definition. The source lines were not available, so this reading is inferred from the message text alone.

## Fix

Open the PDSC file at the line given in the message and check whether the file is listed twice for the same component or in two components that should not share it. Remove or rename the duplicate entry so each file category and name is defined once per component.

## Note

Source lines were not provided, so the trigger condition and the exact duplicate scope (same component versus whole pack) are unverified. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available; message text only)`
