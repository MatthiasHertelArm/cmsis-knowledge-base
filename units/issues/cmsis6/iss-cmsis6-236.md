---
id: "iss-cmsis6-236"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: IAR C++ compile of startup .c: attribute does not apply to any entity"
summary: "CMSIS expects .c files to be compiled as C; in C++ mode IAR maps __NO_RETURN to [[noreturn]], which is invalid inside an extern \"C\" declaration."
status: "draft"
tool: "cmsis-core"
symptoms: ["Error[Pe1866]: attribute does not apply to any entity"]
symptom_regex: "Error\\[Pe1866\\]:\\s+attribute\\s+does\\s+not\\s+apply\\s+to\\s+any\\s+entity"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/236"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/236"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error[Pe1866]: attribute does not apply to any entity`

## Cause

CMSIS expects .c files to be compiled as C; in C++ mode IAR maps __NO_RETURN to [[noreturn]], which is invalid inside an extern "C" declaration.

## Fix

Compile .c files in C mode.

## Source

Resolution: user-error

From [ARM-software/CMSIS_6 #236](https://github.com/ARM-software/CMSIS_6/issues/236), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
