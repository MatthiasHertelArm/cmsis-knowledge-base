---
id: "iss-devtools-786"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk printed nothing when PACK.xsd could not be found"
summary: "packchk looks for the schema in ./, ../etc/ and ../../etc/ relative to the executable and used to stay silent when it was absent."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M218:\n  Unable to find PACK.xsd schema file. Searched in './, ../etc/, ../../etc/' relative to '<path>'."]
symptom_regex: "Unable\\s+to\\s+find\\s+PACK\\.xsd\\s+schema\\s+file\\.\\s+Searched\\s+in\\s+'.*?'\\s+relative\\s+to\\s+'.*?'\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/786"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/786"
resolution: "fixed-in-release"
versions: "fixed in packchk 1.4.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M218:
  Unable to find PACK.xsd schema file. Searched in './, ../etc/, ../../etc/' relative to '<path>'.`

## Cause

packchk looks for the schema in ./, ../etc/ and ../../etc/ relative to the executable and used to stay silent when it was absent.

## Fix

Place PACK.xsd in one of those folders or pass --xsd <file>. Since packchk 1.4.0 error M218 states the searched folders and M219 reports a bad --xsd path.

## Source

Resolution: fixed-in-release

Versions: fixed in packchk 1.4.0

From [Open-CMSIS-Pack/devtools #786](https://github.com/Open-CMSIS-Pack/devtools/issues/786), summarized in own words; confidence high, not reviewed yet.
