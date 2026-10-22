---
id: "ts-svdconv-m129"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M129: Option unknown: …'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M129"
symptoms: ["M129", "Option unknown: %OPT%'"]
symptom_regex: "^Option unknown: .+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check given option 'OPT'."
summary: "An option on the svdconv command line is not known."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/ParseOptions.cpp:403-430", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/ParseOptions.cpp:125-150", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/ParseOptions.cpp:549-552", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:59"]
---

## Symptom

`M129`
`Option unknown: %OPT%'`

## Cause

An option on the svdconv command line is not known.

## Fix

Check the option against svdconv -h and correct its spelling.

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:59) and the README (README.md:238). Unknown options make cxxopts print '<program> error: ...' (exit 1); unknown values of --generate, --fields and --debug are silently ignored.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/ParseOptions.cpp:403-430`
- `tools/svdconv/SVDConv/src/ParseOptions.cpp:125-150`
- `tools/svdconv/SVDConv/src/ParseOptions.cpp:549-552`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:59`
