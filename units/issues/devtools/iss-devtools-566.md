---
id: "iss-devtools-566"
type: "troubleshooting"
domain: "project"
title: "csolution: Switching the compiler to GCC gives no component found with identifier errors"
summary: "Some components listed in the project have toolchain-specific files (for example assembler sources) and are not available for GCC, so csolution cannot resolve them after the compiler is switched; GCC itself is supported by the tools."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: no component was found with identifier 'ARM::Device:Definition'", "error csolution: no component was found with identifier 'Keil::Compiler&ARM Compiler:I/O:STDERR&User'"]
symptom_regex: "no\\s+component\\s+was\\s+found\\s+with\\s+identifier\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/566"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/566"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: no component was found with identifier 'ARM::Device:Definition'`
`error csolution: no component was found with identifier 'Keil::Compiler&ARM Compiler:I/O:STDERR&User'`

## Cause

Some components listed in the project have toolchain-specific files (for example assembler sources) and are not available for GCC, so csolution cannot resolve them after the compiler is switched; GCC itself is supported by the tools.

## Fix

Replace or remove the components that are only available for Arm Compiler when building with GCC.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #566](https://github.com/Open-CMSIS-Pack/devtools/issues/566), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
