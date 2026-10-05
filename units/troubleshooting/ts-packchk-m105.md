---
id: "ts-packchk-m105"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M105: Error while parsing command arguments"
status: "draft"
tool: "packchk"
severity: "error"
code: "M105"
symptoms: ["M105", "Error while parsing command arguments"]
symptom_regex: "^Error while parsing command arguments$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:76", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:200-227", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:334-337", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:24-45", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:124-138"]
---

## Symptom

`M105`
`Error while parsing command arguments`

## Cause

The packchk command line could not be parsed, for example because of an unknown option or an option given without its value.

## Fix

Run packchk -h, correct the options, and give exactly one *.pdsc file as the positional argument, e.g. packchk MyVendor.MyPack.pdsc -i ARM.CMSIS.pdsc.

## Note

No raise site for M105 in packchk at 30f5e81: option errors from cxxopts are printed as '<program> error: <text>' with exit code 1 (ParseOptions.cpp:334-337). Cause inferred from the message text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:76`
- `tools/packchk/src/ParseOptions.cpp:200-227`
- `tools/packchk/src/ParseOptions.cpp:334-337`
- `tools/packchk/README.md:24-45`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:124-138`
