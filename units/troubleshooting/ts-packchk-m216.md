---
id: "ts-packchk-m216"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M216: Unable to get executable path …!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M216"
symptoms: ["M216", "Unable to get executable path %MSG%!"]
symptom_regex: "^Unable to get executable path .+?!$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk was started without --xsd and without --disable-validation, so it looks for PACK.xsd relative to its own executable, but the operating system did not return the executable's path; %MSG% is the system error text."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:102", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:228-237", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:316-332"]
---

## Symptom

`M216`
`Unable to get executable path %MSG%!`

## Cause

packchk was started without --xsd and without --disable-validation, so it looks for PACK.xsd relative to its own executable, but the operating system did not return the executable's path; %MSG% is the system error text. The PDSC is not involved.

## Fix

Pass the schema explicitly with --xsd <path>/PACK.xsd, or skip schema validation with --disable-validation; otherwise start packchk from a normal, readable installation folder.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:102`
- `tools/packchk/src/PackOptions.cpp:228-237`
- `tools/packchk/src/ParseOptions.cpp:316-332`
