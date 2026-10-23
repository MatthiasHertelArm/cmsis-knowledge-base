---
id: "ts-svdconv-m370"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M370: … '…': <offset> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M370"
symptoms: ["M370", "%LEVEL% '%NAME%': <offset> not set."]
symptom_regex: "^.+? '.+?': <offset> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A register has no <addressOffset> (the message calls it <offset>), and no derivedFrom source supplies one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:692", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:694", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:695", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:189"]
---

## Symptom

`M370`
`%LEVEL% '%NAME%': <offset> not set.`

## Cause

A register has no <addressOffset> (the message calls it <offset>), and no derivedFrom source supplies one. The register is dropped.

## Fix

Add <addressOffset> with the register's offset from the peripheral's base address or from the enclosing cluster, for example <addressOffset>0x04</addressOffset>.

## Note

The message names <offset>, but the register element is <addressOffset>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:692`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:694`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:695`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:189`
