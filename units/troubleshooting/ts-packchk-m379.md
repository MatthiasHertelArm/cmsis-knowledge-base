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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "There are no examples found for the board _'BOARD'_. Provide examples. Refer to [/package/examples/example](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example)."
summary: "packchk prints M379 for a board listed in the PDSC that has no example attached to it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M379`
`No example(s) found for Board '[%VENDOR%] %BOARD%'.`

## Cause

packchk prints M379 for a board listed in the PDSC that has no example attached to it. Board names come from the board entries of the pack's device or board description, and the %VENDOR% and %BOARD% placeholders stand for the board's vendor and name as written in the PDSC. The source lines were not available, so this is inferred from the message text and the README rather than from the trigger code.

## Fix

Add at least one example to the PDSC that targets the named board, using the /package/examples/example element described in the Open-CMSIS-Pack specification, so that the board is covered by an example. Then rerun packchk.

## Note

The trigger condition in the source was not checked because the clone was unavailable; the cause and fix rest on the message text and README. The README says 'Provide examples' without specifying which board fields must match, so the exact matching rule is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
