---
id: "iss-toolbox-34"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution 1.6 reports \"reading gpdsc failed\" for a hand-made gpdsc"
summary: "The placeholder gpdsc referenced conditions and generators without defining them; version 1.6.0 validates gpdsc files strictly."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: generator 'STM32CubeMX' from component 'Keil::Device:STM32Cube Framework:STM32CubeMX@2.0.0': reading gpdsc failed"]
symptom_regex: "generator\\s+'.*?'\\s+from\\s+component\\s+'.*?':\\s+reading\\s+gpdsc\\s+failed"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/34"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/34"
resolution: "user-error"
versions: "1.6.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: generator 'STM32CubeMX' from component 'Keil::Device:STM32Cube Framework:STM32CubeMX@2.0.0': reading gpdsc failed`

## Cause

The placeholder gpdsc referenced conditions and generators without defining them; version 1.6.0 validates gpdsc files strictly.

## Fix

Make the gpdsc complete (define conditions and generators) or let the generator create it.

## Source

Resolution: user-error

Versions: 1.6.0

From [Open-CMSIS-Pack/cmsis-toolbox #34](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/34), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
