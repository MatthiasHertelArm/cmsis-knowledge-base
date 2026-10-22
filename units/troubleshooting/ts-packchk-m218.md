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
summary: "packchk could not locate the PACK.xsd schema file that it uses to validate the PDSC."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M218`
`Unable to find PACK.xsd schema file. Searched in '%MSG%' relative to '%PATH%'.   Alternatively use --xsd to specify the location of the schema file.`

## Cause

packchk could not locate the PACK.xsd schema file that it uses to validate the PDSC. It searched the paths named in the message (%MSG% is the searched location, %PATH% the base it was resolved against) and found no file there. This typically happens when the tool installation is incomplete or the schema is not where packchk expects it relative to its own location.

## Fix

Pass the schema location explicitly with --xsd pointing to an existing PACK.xsd, for example: packchk my.pdsc --xsd path/to/PACK.xsd. Alternatively, check that the PACK.xsd file exists at the searched location and reinstall or repair the tool so the schema is present.

## Note

Source lines were not available; cause and fix are derived from the message text and the README's brief note only. The README cause 'Check whether the file exists' is consistent with this reading. Exact search logic was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
