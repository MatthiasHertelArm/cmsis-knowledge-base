---
id: "ts-packchk-m379"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M379: No example(s) found for Board '[…] …'."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M379"
symptoms: ["M379", "No example(s) found for Board '[%VENDOR%] %BOARD%'."]
symptom_regex: "^No example\\(s\\) found for Board '\\[.+?\\] .+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "There are no examples found for the board _'BOARD'_."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:198", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1615-1659", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:217"]
---

## Symptom

`M379`
`No example(s) found for Board '[%VENDOR%] %BOARD%'.`

## Cause

There are no examples found for the board _'BOARD'_. Provide examples. Refer to [/package/examples/example](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example).

## Fix

Add an <example> whose <board name="..." vendor="..."/> matches the board, or pass the pack holding the examples with -i; suppress with -x M379 if the pack has no examples on purpose.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:198`
- `tools/packchk/src/ValidateSyntax.cpp:1615-1659`
- `tools/packchk/README.md:217`
