---
id: "iss-cmsis6-139"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: cmsis_gcc.h: #pragma clang system_header gives an error with -Werror"
summary: "A clang pragma was left in the GCC header."
status: "draft"
tool: "cmsis-core"
symptoms: ["Include/cmsis_gcc.h:28: error: ignoring '#pragma clang system_header' [-Werror=unknown-pragmas]"]
symptom_regex: "Include/cmsis_gcc\\.h:\\S+:\\s+error:\\s+ignoring\\s+'.*?'\\s+\\[\\-Werror=unknown\\-pragmas\\]"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/139"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/139"
resolution: "fixed-in-release"
versions: "6.0.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Include/cmsis_gcc.h:28: error: ignoring '#pragma clang system_header' [-Werror=unknown-pragmas]`

## Cause

A clang pragma was left in the GCC header.

## Fix

Use a CMSIS_6 release including PR 141 (GCC system_header pragma).

## Source

Resolution: fixed-in-release

Versions: 6.0.0

From [ARM-software/CMSIS_6 #139](https://github.com/ARM-software/CMSIS_6/issues/139), summarized in own words; confidence high, not reviewed yet.
