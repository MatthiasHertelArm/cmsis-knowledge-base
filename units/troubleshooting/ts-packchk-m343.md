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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "File _'PATH'_ is defined with the attribute _'ATTR'_ that requires presense of attribute _'ATTR2'_ as well, but such attribute was not found. For example, attr=template requires that attribute select is defined. Add the required attribute _'ATTR2'_ or correct the attribute _'ATTR'_ in the `<file>` element. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "A `<file>` element in the PDSC carries an attribute that depends on a second attribute, for example attr=template, but the required companion attribute (for example select) is missing."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M343`
`File with attribute '%ATTR%' requires '%ATTR2%' attribute: '%PATH%'`

## Cause

A `<file>` element in the PDSC carries an attribute that depends on a second attribute, for example attr=template, but the required companion attribute (for example select) is missing. The message names the file path and the two attribute names involved in that check.

## Fix

Open the `<file>` element named in the message in the PDSC and either add the required companion attribute (for example add select="..." when attr="template") or change or remove the attribute that triggers the requirement.

## Note

The source clone was not available, so the trigger and the attribute pairing are taken from the message and the README only. The README example (attr=template requires select) is not verified against the source.
