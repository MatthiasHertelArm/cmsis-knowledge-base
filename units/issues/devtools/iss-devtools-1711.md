---
id: "iss-devtools-1711"
type: "troubleshooting"
domain: "project"
title: "cbuild: GCC link fails for a Secure project without non-secure callable entries"
summary: "GCC cannot generate a CMSE import library when the secure project exports no cmse entry functions; AC6 only warns."
status: "draft"
tool: "cbuild"
symptoms: ["CM33_s_CMSE_Lib.o: no symbol found for import library", "ld.exe: final link failed: no symbols"]
symptom_regex: "CM33_s_CMSE_Lib\\.o:\\s+no\\s+symbol\\s+found\\s+for\\s+import\\s+library"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1711"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1711"
resolution: "fixed-in-release"
versions: "2.5.0, fixed in 2.6.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CM33_s_CMSE_Lib.o: no symbol found for import library`
`ld.exe: final link failed: no symbols`

## Cause

GCC cannot generate a CMSE import library when the secure project exports no cmse entry functions; AC6 only warns.

## Fix

Set the secure-only option of the trustzone: node under processor: so no import library is generated. Available from CMSIS-Toolbox nightly of September 2024 (2.6.0).

## Source

Resolution: fixed-in-release

Versions: 2.5.0, fixed in 2.6.0

From [Open-CMSIS-Pack/devtools #1711](https://github.com/Open-CMSIS-Pack/devtools/issues/1711), summarized in own words; confidence high, not reviewed yet.
