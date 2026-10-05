---
id: "iss-cmsis6-139"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: cmsis_gcc.h: #pragma clang system_header gives an error with -Werror"
summary: "A clang pragma was left in the GCC header cmsis_gcc.h, which GCC rejects under -Werror=unknown-pragmas."
status: "draft"
tool: "cmsis-core"
symptoms: ["Include/cmsis_gcc.h:28: error: ignoring '#pragma clang system_header' [-Werror=unknown-pragmas]"]
symptom_regex: "Include/cmsis_gcc\\.h:\\S+:\\s+error:\\s+ignoring\\s+'.*?'\\s+\\[\\-Werror=unknown\\-pragmas\\]"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/139"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/139"
resolution: "workaround"
versions: "arm-none-eabi-gcc 13.2.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Include/cmsis_gcc.h:28: error: ignoring '#pragma clang system_header' [-Werror=unknown-pragmas]`

## Cause

A clang pragma was left in the GCC header cmsis_gcc.h, which GCC rejects under -Werror=unknown-pragmas.

## Fix

Replace it with `#pragma GCC system_header` in cmsis_gcc.h, as proposed in PR #141; no merge or release is shown.

## Source

Resolution: workaround

Versions: arm-none-eabi-gcc 13.2.1

From [ARM-software/CMSIS_6 #139](https://github.com/ARM-software/CMSIS_6/issues/139), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
