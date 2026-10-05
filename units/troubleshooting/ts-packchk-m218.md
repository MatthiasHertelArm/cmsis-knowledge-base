---
id: "ts-packchk-m218"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M218: .   Alternatively use --xsd to specify the location of the schema file"
status: "draft"
tool: "packchk"
severity: "error"
code: "M218"
symptoms: ["M218", "Unable to find PACK.xsd schema file. Searched in '%MSG%' relative to '%PATH%'.   Alternatively use --xsd to specify the location of the schema file."]
symptom_regex: "^Unable to find PACK\\.xsd schema file\\. Searched in '.+?' relative to '.+?'\\.   Alternatively use \\-\\-xsd to specify the location of the schema file\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M218`
`Unable to find PACK.xsd schema file. Searched in '%MSG%' relative to '%PATH%'.   Alternatively use --xsd to specify the location of the schema file.`

## Cause

CHeck whether the file exists.

## Fix

_siehe Cause_
