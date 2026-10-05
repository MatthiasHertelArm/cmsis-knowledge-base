---
id: "iss-toolbox-217"
type: "troubleshooting"
domain: "project"
title: "csolution: \"cgen file was not found\" for CubeMX project built with Arm Compiler"
summary: "The csolution.yml still set compiler: AC6 while CubeMX was set to generate for the STM32CubeIDE toolchain (GCC)."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: cgen file was not found, run generator 'CubeMX' for context"]
symptom_regex: "cgen\\s+file\\s+was\\s+not\\s+found,\\s+run\\s+generator\\s+'.*?'\\s+for\\s+context"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/217"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/217"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: cgen file was not found, run generator 'CubeMX' for context`

## Cause

The csolution.yml still set compiler: AC6 while CubeMX was set to generate for the STM32CubeIDE toolchain (GCC).

## Fix

Make the compiler in csolution.yml match the toolchain selected in CubeMX and run the generator again; the maintainer also asked to check that 'Generate Under Root' was disabled after selecting STM32CubeIDE.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/cmsis-toolbox #217](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/217), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
