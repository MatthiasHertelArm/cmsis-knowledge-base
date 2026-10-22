---
id: "ts-svdconv-m120"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M120: Invalid arguments!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M120"
symptoms: ["M120", "Invalid arguments!"]
symptom_regex: "^Invalid arguments!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Provide a list of valid arguments."
summary: "svdconv rejected its command line."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/ParseOptions.cpp:403-430", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/ParseOptions.cpp:549-552", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:133-140", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:50"]
---

## Symptom

`M120`
`Invalid arguments!`

## Cause

svdconv rejected its command line.

## Fix

Call svdconv with one SVD file and supported options only; svdconv -h lists them (-o/--outdir, --generate=header|partition|sfd|sfr|peripheralMap|registerMap|fieldMap, --fields=struct|struct-ansic|macro|enum, --strict, -b/--log, -x/--diag-suppress, --create-folder, ...).

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:50) and the README (README.md:229). Option errors are printed by cxxopts as '<program> error: <text>' and svdconv exits with 1, although the README return-code table says 3.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/ParseOptions.cpp:403-430`
- `tools/svdconv/SVDConv/src/ParseOptions.cpp:549-552`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:133-140`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:50`
