---
id: "ts-packchk-m371"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M371: … Feature for '…': '…' unknown."
status: "draft"
tool: "packchk"
severity: "error"
code: "M371"
symptoms: ["M371", "%SECTION% Feature for '%MCU%': '%FEATURE%' unknown."]
symptom_regex: "^.+? Feature for '.+?': '.+?' unknown\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "This feature _'FEATURE'_ is unknwon to the specified _'MCU'_."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:190", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:616-767", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:775-859", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:952-960", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:498-526", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:209"]
---

## Symptom

`M371`
`%SECTION% Feature for '%MCU%': '%FEATURE%' unknown.`

## Cause

This feature _'FEATURE'_ is unknwon to the specified _'MCU'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)) if this is a typo.

## Fix

Use a feature type packchk knows, spelled exactly, e.g. device features such as "NVIC", "UART", "QFP" or board features such as "ODbg", "LED", "Button": <feature type="UART" n="4"/>. The check runs only when schemaVersion is above 1.1.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:190`
- `tools/packchk/src/ValidateSyntax.cpp:616-767`
- `tools/packchk/src/ValidateSyntax.cpp:775-859`
- `tools/packchk/src/ValidateSyntax.cpp:952-960`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:498-526`
- `tools/packchk/README.md:209`
