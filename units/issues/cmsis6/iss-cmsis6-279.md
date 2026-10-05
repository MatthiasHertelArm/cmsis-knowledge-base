---
id: "iss-cmsis6-279"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: IAR rejects __NO_RETURN in a function pointer typedef"
summary: "For IAR the macro maps to the C11 _Noreturn keyword, which is invalid in a function pointer type."
status: "draft"
tool: "cmsis-core"
symptoms: ["Error[Pe2529]: _Noreturn is not allowed here"]
symptom_regex: "Error\\[Pe2529\\]:\\s+_Noreturn\\s+is\\s+not\\s+allowed\\s+here"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/279"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/279"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error[Pe2529]: _Noreturn is not allowed here`

## Cause

For IAR the macro maps to the C11 _Noreturn keyword, which is invalid in a function pointer type.

## Fix

Use __attribute__((__noreturn__)) directly there (needs language extensions on IAR). A CMSIS_6 change (PR 284) falls back to the attribute when available.

## Source

Resolution: fixed-in-release

From [ARM-software/CMSIS_6 #279](https://github.com/ARM-software/CMSIS_6/issues/279), summarized in own words; confidence medium, not reviewed yet.
