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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "`<memory>` element requires that either attribute id or attributes name and access are specified, but none of those were found."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:121", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:237-241", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:156"]
---

## Symptom

`M307`
`Either attribute '%TAG%' or '%TAG2%' + '%TAG3%' must be specified for 'memory'`

## Cause

`<memory>` element requires that either attribute id or attributes name and access are specified, but none of those were found. Specify the expected attributes. Refer to [/package/devices/family/.../memory](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory).

## Fix

Describe each memory either with id (legacy IROM1/IRAM1 form) or with name plus access, e.g. <memory name="Flash" access="rx" start="0x08000000" size="0x00080000" startup="1"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:121`
- `tools/packchk/src/ValidateSemantic.cpp:237-241`
- `tools/packchk/README.md:156`
