---
id: "iss-devtools-1711"
type: "troubleshooting"
domain: "project"
title: "cbuild: GCC link fails for a Secure project without non-secure callable entries"
summary: "GCC cannot generate a CMSE import library when the secure project has no non-secure callable entry functions and fails the link; AC6 only warns."
status: "draft"
tool: "cbuild"
symptoms: ["CM33_s_CMSE_Lib.o: no symbol found for import library", "ld.exe: final link failed: no symbols"]
symptom_regex: "CM33_s_CMSE_Lib\\.o:\\s+no\\s+symbol\\s+found\\s+for\\s+import\\s+library"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1711"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1711"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CM33_s_CMSE_Lib.o: no symbol found for import library`
`ld.exe: final link failed: no symbols`

## Cause

GCC cannot generate a CMSE import library when the secure project has no non-secure callable entry functions and fails the link; AC6 only warns.

## Fix

Set secure-only in the trustzone: node under processor:, so no import library is generated for that project; validated with the CMSIS-Toolbox nightly of 2024-09-03.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #1711](https://github.com/Open-CMSIS-Pack/devtools/issues/1711), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
