---
id: "ts-packchk-m342"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M342: File with attribute '…' must not have category '…': '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M342"
symptoms: ["M342", "File with attribute '%ATTR%' must not have category '%CAT%': '%PATH%'"]
symptom_regex: "^File with attribute '.+?' must not have category '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "File _'PATH'_ is defined with the attribute attr set to _'ATTR'_. This conflicts with the file category _'CAT'_ specified in category attribute. For example attr=config and category=include are not allowed for the same file. Correct the file attribute or the file category. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "A <file> with attr=\"template\" also has category=\"include\"; packchk does not allow templates to be include folders."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:160", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:382-384", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:649-679", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:183"]
---

## Symptom

`M342`
`File with attribute '%ATTR%' must not have category '%CAT%': '%PATH%'`

## Cause

A <file> with attr="template" also has category="include"; packchk does not allow templates to be include folders. Only attr="template" is checked here, not attr="config" as the README example says.

## Fix

Give the template a file category such as sourceC or header, or remove attr="template" from the include entry.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:160`
- `tools/packchk/src/CheckFiles.cpp:382-384`
- `tools/packchk/src/CheckFiles.cpp:649-679`
- `tools/packchk/README.md:183`
