---
id: "ts-packchk-m372"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M372: … Feature for '…': '…' misspelled, did you mean '…' (…)."
status: "draft"
tool: "packchk"
severity: "error"
code: "M372"
symptoms: ["M372", "%SECTION% Feature for '%MCU%': '%FEATURE%' misspelled, did you mean '%KNOWNFEATURE%' (%DESCR%)."]
symptom_regex: "^.+? Feature for '.+?': '.+?' misspelled, did you mean '.+?' \\(.+?\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "This feature _'FEATURE'_ resembles the feature _'KNOWNFEATURE'_."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:191", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:793-805", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:839-851", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:210"]
---

## Symptom

`M372`
`%SECTION% Feature for '%MCU%': '%FEATURE%' misspelled, did you mean '%KNOWNFEATURE%' (%DESCR%).`

## Cause

This feature _'FEATURE'_ resembles the feature _'KNOWNFEATURE'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)) if this is a typo.

## Fix

Write the type with the spelling suggested in the message, e.g. type="UART" instead of type="Uart".

## Note

For board features the name in the message is the feature's name attribute, not the board name (ValidateSyntax.cpp:1225).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:191`
- `tools/packchk/src/ValidateSyntax.cpp:793-805`
- `tools/packchk/src/ValidateSyntax.cpp:839-851`
- `tools/packchk/README.md:210`
