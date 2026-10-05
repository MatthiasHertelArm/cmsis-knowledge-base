---
id: "ts-packchk-m343"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M343: File with attribute '…' requires '…' attribute: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M343"
symptoms: ["M343", "File with attribute '%ATTR%' requires '%ATTR2%' attribute: '%PATH%'"]
symptom_regex: "^File with attribute '.+?' requires '.+?' attribute: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:161", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:649-679", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:184"]
---

## Symptom

`M343`
`File with attribute '%ATTR%' requires '%ATTR2%' attribute: '%PATH%'`

## Cause

File _'PATH'_ is defined with the attribute _'ATTR'_ that requires presense of attribute _'ATTR2'_ as well, but such attribute was not found. For example, attr=template requires that attribute select is defined. Add the required attribute _'ATTR2'_ or correct the attribute _'ATTR'_ in the `<file>` element. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

Add select with a short label for the template, e.g. <file category="sourceC" attr="template" name="Templates/main.c" select="Main module"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:161`
- `tools/packchk/src/CheckFiles.cpp:649-679`
- `tools/packchk/README.md:184`
