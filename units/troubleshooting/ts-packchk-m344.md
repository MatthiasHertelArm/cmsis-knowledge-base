---
id: "ts-packchk-m344"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M344: File shall have condition containing '…': '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M344"
symptoms: ["M344", "File shall have condition containing '%COND%': '%PATH%'"]
symptom_regex: "^File shall have condition containing '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "File definition for _'PATH'_ shall contain a condition _'COND'_. Add attribute condition with the _'COND'_ in the `<file>` tag that defines the _'PATH'_ file. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "packchk prints this warning when a file entry in the PDSC lacks a condition attribute that the check requires, so the file's %PATH% entry is missing a condition containing %COND%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)"]
---

## Symptom

`M344`
`File shall have condition containing '%COND%': '%PATH%'`

## Cause

packchk prints this warning when a file entry in the PDSC lacks a condition attribute that the check requires, so the file's %PATH% entry is missing a condition containing %COND%. The README states the file definition must carry a condition with the named value on the <file> element that defines the file.

## Fix

Add a condition attribute to the <file> element that defines the file named in the message, using a condition whose name contains the value shown as %COND%, for example <file category="..." name="%PATH%" condition="%COND%"/>. Check the PDSC for the <file> line whose name matches the path in the message.

## Note

Answered from the message text and README only, since the source clone was not available; the exact trigger condition in PackChk_Msgs.cpp is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)`
