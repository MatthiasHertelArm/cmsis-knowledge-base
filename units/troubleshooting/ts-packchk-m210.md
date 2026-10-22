---
id: "ts-packchk-m210"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M210: Only one input file to be checked is allowed."
status: "draft"
tool: "packchk"
severity: "error"
code: "M210"
symptoms: ["M210", "Only one input file to be checked is allowed."]
symptom_regex: "^Only one input file to be checked is allowed\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "You can only check one PDSC file at a time."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:96", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:208", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:226", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:137"]
---

## Symptom

`M210`
`Only one input file to be checked is allowed.`

## Cause

You can only check one PDSC file at a time.

## Fix

Run packchk once per PDSC; pass packs it depends on with -i instead of as extra file arguments.

## Note

No raise site for M210 in packchk at 30f5e81; fix inferred from the message and README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:96`
- `tools/packchk/src/ParseOptions.cpp:208`
- `tools/packchk/src/ParseOptions.cpp:226`
- `tools/packchk/README.md:137`
