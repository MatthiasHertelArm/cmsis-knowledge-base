---
id: "iss-devtools-735"
type: "troubleshooting"
domain: "project"
title: "cbuild: GCC link error undefined reference to log10 because -lm is placed before the objects"
summary: "Everything under misc: Link: is put in front of the object files in the linker command line, so -lm and similar libraries are not resolved."
status: "draft"
tool: "cbuild"
symptoms: ["ARMCM0.GCC/math_helper.c:103: undefined reference to `log10'"]
symptom_regex: "ARMCM0\\.GCC/math_helper\\.c:\\S+:\\s+undefined\\s+reference\\s+to\\s+`log10'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/735"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/735"
resolution: "fixed-in-release"
versions: "fixed in 1.7.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ARMCM0.GCC/math_helper.c:103: undefined reference to `log10'`

## Cause

Everything under misc: Link: is put in front of the object files in the linker command line, so -lm and similar libraries are not resolved.

## Fix

Use the new misc: Library: node (for example - -lm - -lc - -lgcc - -lnosys), which is placed after the objects. Available since CMSIS-Toolbox 1.7.0.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.7.0

From [Open-CMSIS-Pack/devtools #735](https://github.com/Open-CMSIS-Pack/devtools/issues/735), summarized in own words; confidence high, checked against the thread, not reviewed yet.
