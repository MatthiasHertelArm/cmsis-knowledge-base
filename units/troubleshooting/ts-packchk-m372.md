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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "This feature _'FEATURE'_ resembles the feature _'KNOWNFEATURE'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)) if this is a typo."
summary: "packchk prints this when a feature element in a PDSC device family or variant has a name that is close to, but not exactly, a feature name it recognises, so it suspects a typo."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)"]
---

## Symptom

`M372`
`%SECTION% Feature for '%MCU%': '%FEATURE%' misspelled, did you mean '%KNOWNFEATURE%' (%DESCR%).`

## Cause

packchk prints this when a feature element in a PDSC device family or variant has a name that is close to, but not exactly, a feature name it recognises, so it suspects a typo. The %FEATURE% value is the name written in the PDSC, %KNOWNFEATURE% is the recognised name it suggests, and %SECTION% and %MCU% say where the element sits. The source lines were not available, so this reading comes from the message text and the README description only.

## Fix

Open the PDSC at the device family or variant named in the message, find the feature element whose name is the misspelled value, and correct it to the suggested feature name, then rerun packchk.

## Note

The README describes the same check, but the trigger condition and the exact fuzzy-match rule could not be confirmed from source. The README link path uses '/package/devices/family/.../feature', which is a placeholder pattern rather than a literal path.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)`
