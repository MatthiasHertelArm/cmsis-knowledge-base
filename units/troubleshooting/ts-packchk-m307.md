---
id: "ts-packchk-m307"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M307: Either attribute '…' or '…' + '…' must be specified for 'memory'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M307"
symptoms: ["M307", "Either attribute '%TAG%' or '%TAG2%' + '%TAG3%' must be specified for 'memory'"]
symptom_regex: "^Either attribute '.+?' or '.+?' \\+ '.+?' must be specified for 'memory'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "`<memory>` element requires that either attribute id or attributes name and access are specified, but none of those were found. Specify the expected attributes. Refer to [/package/devices/family/.../memory](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory)."
summary: "packchk prints this when a PDSC `<memory>` element has neither an `id` attribute nor the pair `name` plus `access`."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M307`
`Either attribute '%TAG%' or '%TAG2%' + '%TAG3%' must be specified for 'memory'`

## Cause

packchk prints this when a PDSC `<memory>` element has neither an `id` attribute nor the pair `name` plus `access`. The placeholders %TAG%, %TAG2% and %TAG3% stand for the attribute names the rule expects (id, or name and access). The source lines were not available, so this is taken from the message text and the README rather than from the trigger code.

## Fix

Open the `<memory>` element in the PDSC file named in the log and either add an `id` attribute, or add both `name` and `access` attributes, as the device family memory element specification describes.

## Note

Source lines were not available, so the trigger condition is inferred from the message wording and the README, not verified in code. The message text names one alternative as a single attribute and the other as a pair, which matches the README cause.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
