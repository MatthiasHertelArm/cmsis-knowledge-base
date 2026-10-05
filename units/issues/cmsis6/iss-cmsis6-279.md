---
id: "iss-cmsis6-279"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: IAR rejects __NO_RETURN in a function pointer typedef"
summary: "For IAR the macro maps to the C11 _Noreturn keyword (since CMSIS_6 PR #85), which is not allowed in a function pointer type."
status: "draft"
tool: "cmsis-core"
symptoms: ["Error[Pe2529]: _Noreturn is not allowed here"]
symptom_regex: "Error\\[Pe2529\\]:\\s+_Noreturn\\s+is\\s+not\\s+allowed\\s+here"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/279"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/279"
resolution: "workaround"
versions: "CMSIS 5.8.2 works; CMSIS 6 fails"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error[Pe2529]: _Noreturn is not allowed here`

## Cause

For IAR the macro maps to the C11 _Noreturn keyword (since CMSIS_6 PR #85), which is not allowed in a function pointer type.

## Fix

Use __attribute__((__noreturn__)) directly in the typedef (needs language extensions on IAR). The maintainers planned to use the attribute when __has_attribute reports it and asked the reporter to check PR #284; no confirmation in the thread.

## Source

Resolution: workaround

Versions: CMSIS 5.8.2 works; CMSIS 6 fails

From [ARM-software/CMSIS_6 #279](https://github.com/ARM-software/CMSIS_6/issues/279), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
