---
id: "ts-packchk-m218"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M218: Unable to find PACK.xsd schema file. Searched in '…' relative to '…'. Alternatively use --xsd to …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M218"
symptoms: ["M218", "Unable to find PACK.xsd schema file. Searched in '%MSG%' relative to '%PATH%'.   Alternatively use --xsd to specify the location of the schema file."]
symptom_regex: "^Unable to find PACK\\.xsd schema file\\. Searched in '.+?' relative to '.+?'\\.   Alternatively use \\-\\-xsd to specify the location of the schema file\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "CHeck whether the file exists."
summary: "No --xsd option was given and packchk found no PACK.xsd in ./, ../etc/ or ../../etc/ relative to the folder of its executable (%PATH%), so it cannot run the schema check."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:104", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:228-265", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:316-332", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:54-57", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:138"]
---

## Symptom

`M218`
`Unable to find PACK.xsd schema file. Searched in '%MSG%' relative to '%PATH%'.   Alternatively use --xsd to specify the location of the schema file.`

## Cause

No --xsd option was given and packchk found no PACK.xsd in ./, ../etc/ or ../../etc/ relative to the folder of its executable (%PATH%), so it cannot run the schema check. The README row for M218 describes the --xsd case, which is M219.

## Fix

Pass the schema with --xsd <path>/PACK.xsd, or run packchk from a CMSIS-Toolbox installation where etc/PACK.xsd sits next to bin/, or skip the schema check with --disable-validation.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:104`
- `tools/packchk/src/PackOptions.cpp:228-265`
- `tools/packchk/src/ParseOptions.cpp:316-332`
- `tools/packchk/README.md:54-57`
- `tools/packchk/README.md:138`
