---
id: "ts-packchk-m214"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M214: Invalid argument: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M214"
symptoms: ["M214", "Invalid argument: %OPT%"]
symptom_regex: "^Invalid argument: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A packchk command-line argument was not accepted; %OPT% names it."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:100", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:200-227", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:334-337", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:24-45"]
---

## Symptom

`M214`
`Invalid argument: %OPT%`

## Cause

A packchk command-line argument was not accepted; %OPT% names it.

## Fix

Check the named option against packchk -h and correct its spelling or value; for example -w takes 0, 1, 2, 3 or all.

## Note

No raise site for M214 in packchk at 30f5e81 (the code M214 is only raised by svdconv); invalid options are reported by cxxopts as '<program> error: <text>'. Cause inferred from the message text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:100`
- `tools/packchk/src/ParseOptions.cpp:200-227`
- `tools/packchk/src/ParseOptions.cpp:334-337`
- `tools/packchk/README.md:24-45`
