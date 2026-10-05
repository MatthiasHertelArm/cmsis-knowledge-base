---
id: "iss-devtools-1659"
type: "troubleshooting"
domain: "project"
title: "csolution: Schema check failed when compiler: is set to LLVM"
summary: "The value of compiler: must be one of GCC, CLANG, AC6 or IAR; LLVM is not valid, so the schema check fails at the compiler node."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: schema check failed, verify syntax"]
symptom_regex: "schema\\s+check\\s+failed,\\s+verify\\s+syntax"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1659"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1659"
resolution: "user-error"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"], "toolchain": ["CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: schema check failed, verify syntax`

## Cause

The value of compiler: must be one of GCC, CLANG, AC6 or IAR; LLVM is not valid, so the schema check fails at the compiler node.

## Fix

Use compiler: CLANG for LLVM-based toolchains.

## Source

Resolution: user-error

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1659](https://github.com/Open-CMSIS-Pack/devtools/issues/1659), summarized in own words; confidence high, checked against the thread, not reviewed yet.
