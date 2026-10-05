---
id: "ts-svdconv-m302"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M302: Size of Register '…:…' must be 8, 16 or 32 Bits"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M302"
symptoms: ["M302", "Size of Register '%NAME%:%NUM%' must be 8, 16 or 32 Bits"]
symptom_regex: "^Size of Register '.+?:.+?' must be 8, 16 or 32 Bits$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:85", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:94", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:95", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:96", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:121", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:233"]
---

## Symptom

`M302`
`Size of Register '%NAME%:%NUM%' must be 8, 16 or 32 Bits`

## Cause

A register's own <size> is not a width svdconv supports. The code accepts 8, 16, 24, 32 and 64 bits although the message names only 8, 16 and 32, and the register is dropped even though the message is a warning (an error with --strict).

## Fix

Set the register's <size> to its access width, normally 8, 16 or 32 on Cortex-M devices. A register with fewer implemented bits still uses the full access width and simply has fields only for the implemented bits.

## Note

Message text is incomplete: 24 and 64 are accepted too.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:85`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:94`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:95`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:96`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:121`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:233`
