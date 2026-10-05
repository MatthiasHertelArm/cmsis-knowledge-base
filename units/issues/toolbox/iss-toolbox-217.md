---
id: "iss-toolbox-217"
type: "troubleshooting"
domain: "project"
title: "csolution: \"cgen file was not found\" for CubeMX project built with Arm Compiler"
summary: "The CubeMX toolchain/IDE setting did not match the compiler of the solution (solution still used AC6 while CubeMX generated for CubeIDE), and generation under the root folder must stay enabled."
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
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: cgen file was not found, run generator 'CubeMX' for context`

## Cause

The CubeMX toolchain/IDE setting did not match the compiler of the solution (solution still used AC6 while CubeMX generated for CubeIDE), and generation under the root folder must stay enabled.

## Fix

Make the generator toolchain selection match the compiler in csolution.yml and keep Generate Under Root enabled, then run the generator again.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/cmsis-toolbox #217](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/217), summarized in own words; confidence medium, not reviewed yet.
