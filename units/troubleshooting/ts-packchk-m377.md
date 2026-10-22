---
id: "ts-packchk-m377"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M377: File '…' … must have 'attr=\"config\"'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M377"
symptoms: ["M377", "File '%NAME%' %TYPE% must have 'attr=\"config\"'"]
symptom_regex: "^File '.+?' .+? must have 'attr=\"config\"'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The category _'TYPE'_ of the file _'NAME'_ requires it to be defined as a configuration file. Add the attribute attr=\"config\" to the `<file>` element that defines the file. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "packchk prints M377 when a PDSC file entry of a category that must be a configuration file (the %TYPE% placeholder, e.g. config) lacks attr=\"config\" on its <file> element."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; trigger line not available)"]
---

## Symptom

`M377`
`File '%NAME%' %TYPE% must have 'attr="config"'`

## Cause

packchk prints M377 when a PDSC file entry of a category that must be a configuration file (the %TYPE% placeholder, e.g. config) lacks attr="config" on its <file> element. The %NAME% placeholder is the file name as written in the PDSC. The README states this requirement, but the source lines were not available to confirm the exact trigger condition.

## Fix

Open the PDSC file, find the <file> element that names the file given in the message, and add attr="config" to it, for example <file category="header" name="Config/config.h" attr="config"/> with the category and name kept as they are, then rerun packchk.

## Note

Source lines were not available, so the trigger condition and the exact set of categories requiring attr="config" are taken from the README and message text only. The example element is illustrative; the category shown should be checked against the file's actual category.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; trigger line not available)`
