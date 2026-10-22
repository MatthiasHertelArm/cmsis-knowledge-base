---
id: "ts-packchk-m337"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M337: File with category '…' has wrong extension '…': '…'…"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M337"
symptoms: ["M337", "File with category '%CAT%' has wrong extension '%EXT%': '%PATH%'%MSG%"]
symptom_regex: "^File with category '.+?' has wrong extension '.+?': '.+?'.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The extension of the file does not match the file category _'CAT'_ specified in the category attribute. Verify the extension to match the category. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "The PDSC `<file>` entry names a file whose extension does not fit the `category` attribute it declares."
cause_origin: "source-analysis"
confidence: "low"
---

## Symptom

`M337`
`File with category '%CAT%' has wrong extension '%EXT%': '%PATH%'%MSG%`

## Cause

The PDSC `<file>` entry names a file whose extension does not fit the `category` attribute it declares. The message's %CAT% is that category, %EXT% is the file's extension, and %PATH% is the file path. The source lines were not available, so the trigger check could not be confirmed and this comes from the README text.

## Fix

Check the `category` attribute on the flagged `<file>` element in the PDSC against the file's extension. Either rename the file so its extension matches the category, or change the `category` to the one that fits the file. Then rerun packchk.

## Note

The source clone was unavailable, so no path:line evidence was checked and the trigger condition is unverified. The fix is taken from the README and was not confirmed against the source. The message has a %MSG% suffix whose content is unknown here.
