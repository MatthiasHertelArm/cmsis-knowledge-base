---
id: "ts-packchk-m326"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M326: Path is not conformant: '…': Absolute Paths or Drive references are not allowed, use Paths relative …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M326"
symptoms: ["M326", "Path is not conformant: '%PATH%':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file."]
symptom_regex: "^Path is not conformant: '.+?':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The path needs to be relative to the PDSC file so that a dependency of a certain file system does not occur."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:142", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:52-67", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:430-433", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:155-174", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:167"]
---

## Symptom

`M326`
`Path is not conformant: '%PATH%':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file.`

## Cause

The path needs to be relative to the PDSC file so that a dependency of a certain file system does not occur.

## Fix

Write the path relative to the folder of the PDSC, e.g. name="Source/startup.c" instead of "C:/work/pack/Source/startup.c" or "/boards/...".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:142`
- `tools/packchk/src/RteModelReader.cpp:52-67`
- `tools/packchk/src/CheckFiles.cpp:430-433`
- `tools/packchk/src/ValidateSyntax.cpp:155-174`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247`
- `tools/packchk/README.md:167`
