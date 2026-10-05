---
id: "iss-cmsis6-259"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: GCC -Warray-bounds warning from __TZ_set_STACKSEAL_S in startup file"
summary: "The linker symbol __StackSeal is 64 bit but was declared as uint32_t in the startup template."
status: "draft"
tool: "cmsis-core"
symptoms: ["warning: array subscript 'uint64_t {aka long long unsigned int}[0]' is partly outside array bounds of 'uint32_t[1]' {aka 'long unsigned int[1]'} [-Warray-bounds=]"]
symptom_regex: "array\\s+subscript\\s+'.*?'\\s+is\\s+partly\\s+outside\\s+array\\s+bounds\\s+of\\s+'.*?'\\s+\\{aka\\s+'.*?'\\}\\s+\\[\\-Warray\\-bounds=\\]"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/259"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/259"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning: array subscript 'uint64_t {aka long long unsigned int}[0]' is partly outside array bounds of 'uint32_t[1]' {aka 'long unsigned int[1]'} [-Warray-bounds=]`

## Cause

The linker symbol __StackSeal is 64 bit but was declared as uint32_t in the startup template.

## Fix

Declare __STACK_SEAL as extern uint64_t in the startup file; the reporter opened PRs for the CMSIS_6 template (#260) and for Cortex_DFP (#22).

## Source

Resolution: fixed-in-release

From [ARM-software/CMSIS_6 #259](https://github.com/ARM-software/CMSIS_6/issues/259), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
