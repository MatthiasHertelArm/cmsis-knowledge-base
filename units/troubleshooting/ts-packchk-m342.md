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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "File _'PATH'_ is defined with the attribute attr set to _'ATTR'_. This conflicts with the file category _'CAT'_ specified in category attribute. For example attr=config and category=include are not allowed for the same file. Correct the file attribute or the file category. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "A file entry in the PDSC has an attr value (here the attribute named by %ATTR%) combined with a category (%CAT%) that the CMSIS-Pack specification does not allow together for the same file, so packchk flags the file at %PATH%."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M342`
`File with attribute '%ATTR%' must not have category '%CAT%': '%PATH%'`

## Cause

A file entry in the PDSC has an attr value (here the attribute named by %ATTR%) combined with a category (%CAT%) that the CMSIS-Pack specification does not allow together for the same file, so packchk flags the file at %PATH%. The README gives the example attr=config with category=include as a forbidden combination.

## Fix

Open the <file> element at the path shown in the message in the PDSC and either change its attr attribute or its category attribute so the pair is allowed by the Pack specification (for example, remove the config attribute or use a category that fits config files). Then rerun packchk.

## Note

The clone was not available, so the trigger and handling could not be read from source; cause and fix rest on the message text and the README. The README cause and fix were used as the basis for this entry.
