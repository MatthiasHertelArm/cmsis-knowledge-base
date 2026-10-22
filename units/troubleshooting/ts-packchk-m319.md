---
id: "ts-packchk-m319"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M319: '…': '…' already defined for '…': '…', see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M319"
symptoms: ["M319", "'%TAG%': '%NAME%' already defined for '%TAG2%': '%NAME2%', see Line %LINE%"]
symptom_regex: "^'.+?': '.+?' already defined for '.+?': '.+?', see Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk found the same identifier defined twice for one element type inside the pack description, so one definition collides with an earlier one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M319`
`'%TAG%': '%NAME%' already defined for '%TAG2%': '%NAME2%', see Line %LINE%`

## Cause

packchk found the same identifier defined twice for one element type inside the pack description, so one definition collides with an earlier one. The %TAG% and %NAME% fields name the element kind and its name that was already defined, %TAG2% and %NAME2% name the element that clashes with it, and %LINE% gives the line of the earlier definition. The source lines were not available, so this reading comes from the message text alone.

## Fix

Open the PDSC file at the line given in the message and find the second element with the same name. Rename it or remove the duplicate so that each name is defined once for its element type, then run packchk again.

## Note

Trigger and handling were not checked against source lines because the clone is not available; cause and fix are inferred from the message text alone.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
