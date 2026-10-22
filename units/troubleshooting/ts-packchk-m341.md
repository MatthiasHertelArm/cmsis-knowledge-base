---
id: "ts-packchk-m341"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M341: File with '…' dependency must have extension '…': '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M341"
symptoms: ["M341", "File with '%COMP%' dependency must have extension '%EXT%': '%PATH%'"]
symptom_regex: "^File with '.+?' dependency must have extension '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The file _'PATH'_ with dependency on component _'COMP'_ must have a specific extension _'EXT'_. Verify the dependency and correct the file extension. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "packchk prints M341 when a PDSC file entry that carries a component dependency has a file name whose extension does not match the extension required for that dependency type."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text M341 as given in the message id, trigger not visible)"]
---

## Symptom

`M341`
`File with '%COMP%' dependency must have extension '%EXT%': '%PATH%'`

## Cause

packchk prints M341 when a PDSC file entry that carries a component dependency has a file name whose extension does not match the extension required for that dependency type. The %COMP% placeholder names the component the dependency refers to, %EXT% the extension it expects, and %PATH% the offending file path as written in the PDSC. The source lines were not available, so this reading comes from the message text and the README rather than from the trigger code.

## Fix

Open the PDSC file, find the <file> element with the path shown in the message and the dependency on the named component, then correct the file name so that it ends with the required extension (for example rename the file or change the path in the <file> element to match the expected extension). Run packchk again to confirm the warning is gone.

## Note

Source lines were not provided, so the trigger condition is inferred from the message wording and the README; the exact extension check could not be verified. The README links to the PDSC components page for the file element.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text M341 as given in the message id, trigger not visible)`
