---
id: "ts-packchk-m379"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M379: No example(s) found for Board '["
status: "draft"
tool: "packchk"
severity: "warning"
code: "M379"
symptoms: ["M379", "No example(s) found for Board '[%VENDOR%] %BOARD%'."]
symptom_regex: "^No example\\(s\\) found for Board '\\[.+?\\] .+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M379`
`No example(s) found for Board '[%VENDOR%] %BOARD%'.`

## Cause

There are no examples found for the board _'BOARD'_. Provide examples. Refer to [/package/examples/example](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example).

## Fix

_siehe Cause_
