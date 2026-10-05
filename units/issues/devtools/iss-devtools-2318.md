---
id: "iss-devtools-2318"
type: "troubleshooting"
domain: "project"
title: "csolution: GCC link errors with generated linker script and startup file of old STM32F4xx_DFP"
summary: "The old STM32F4xx_DFP (2.17.1) startup file and generated GCC linker script do not match; ST families rely on STM32CubeMX for consistent startup and linker files."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2318"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2318"
resolution: "configuration"
versions: "Keil::STM32F4xx_DFP 2.17.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "family": ["STM32F4 Series"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The old STM32F4xx_DFP (2.17.1) startup file and generated GCC linker script do not match; ST families rely on STM32CubeMX for consistent startup and linker files.

## Fix

Use the latest STM32F4xx_DFP and set the project up with the CubeMX generator as the pack overview and the toolbox CubeMX documentation describe.

## Source

Resolution: configuration

Versions: Keil::STM32F4xx_DFP 2.17.1

From [Open-CMSIS-Pack/devtools #2318](https://github.com/Open-CMSIS-Pack/devtools/issues/2318), summarized in own words; confidence medium, not reviewed yet.
