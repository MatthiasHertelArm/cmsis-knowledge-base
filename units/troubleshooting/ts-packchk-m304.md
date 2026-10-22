---
id: "ts-packchk-m304"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M304: No package URL (<url>-tag and/or value) found in PDSC file!"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M304"
symptoms: ["M304", "No package URL (<url>-tag and/or value) found in PDSC file!"]
symptom_regex: "^No package URL \\(<url>\\-tag and/or value\\) found in PDSC file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Package URL is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<url>` and add the URL that should be used to download the package. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url)."
summary: "packchk found no <url> element with a value inside the <package> element of the PDSC file, so it cannot tell where the package should be downloaded from."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M304 is printed here; the trigger lines were not available to check)"]
---

## Symptom

`M304`
`No package URL (<url>-tag and/or value) found in PDSC file!`

## Cause

packchk found no <url> element with a value inside the <package> element of the PDSC file, so it cannot tell where the package should be downloaded from. The message names the missing tag and value in its placeholder.

## Fix

Open the PDSC file and, inside the top-level <package> element, add a <url> element containing the base URL from which the package is downloaded, for example <url>https://example.com/packs/</url>. Then run packchk again.

## Note

The source clone was not available, so the trigger condition is taken from the message text and the README only. The README cause and fix agree with that reading.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M304 is printed here; the trigger lines were not available to check)`
