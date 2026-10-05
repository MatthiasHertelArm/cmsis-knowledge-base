---
id: "iss-devtools-614"
type: "troubleshooting"
domain: "project"
title: "cbuild: AC6 build of a legacy armasm startup file fails on STM32F1 (GNU syntax assumed)"
summary: "armclang assembles with GNU syntax by default (-masm=gnu), but device startup files such as startup_stm32f10x_md.s use legacy armasm syntax."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/614"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/614"
resolution: "configuration"
versions: "csolution 1.3.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "family": ["STM32F1 Series"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

armclang assembles with GNU syntax by default (-masm=gnu), but device startup files such as startup_stm32f10x_md.s use legacy armasm syntax.

## Fix

Add the assembler option -masm=auto under misc: ASM: (for example in cdefault.yml build-types). Note that Arm Compiler will remove -masm in a later release, so port the file to GNU syntax long term.

## Source

Resolution: configuration

Versions: csolution 1.3.0

From [Open-CMSIS-Pack/devtools #614](https://github.com/Open-CMSIS-Pack/devtools/issues/614), summarized in own words; confidence high, not reviewed yet.
