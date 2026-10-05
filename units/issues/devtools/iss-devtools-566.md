---
id: "iss-devtools-566"
type: "troubleshooting"
domain: "project"
title: "csolution: Switching the compiler to GCC gives no component found with identifier errors"
summary: "The components listed in the project (for example Keil::Compiler&ARM Compiler:... or ARM::Device:Definition) exist only for Arm Compiler, so they cannot be resolved for another toolchain."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: no component was found with identifier 'ARM::Device:Definition'", "error csolution: no component was found with identifier 'Keil::Compiler&ARM Compiler:I/O:STDERR&User'"]
symptom_regex: "no\\s+component\\s+was\\s+found\\s+with\\s+identifier\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/566"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/566"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: no component was found with identifier 'ARM::Device:Definition'`
`error csolution: no component was found with identifier 'Keil::Compiler&ARM Compiler:I/O:STDERR&User'`

## Cause

The components listed in the project (for example Keil::Compiler&ARM Compiler:... or ARM::Device:Definition) exist only for Arm Compiler, so they cannot be resolved for another toolchain.

## Fix

Make compiler-specific components conditional with for-compiler: AC6 (and provide a GCC equivalent such as retargeting sources); the toolbox itself supports GCC.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #566](https://github.com/Open-CMSIS-Pack/devtools/issues/566), summarized in own words; confidence high, not reviewed yet.
