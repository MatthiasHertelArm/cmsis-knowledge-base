---
id: "iss-rtx-43"
type: "troubleshooting"
domain: "rtos"
title: "RTX: Compiling RTX for Cortex-A7 gives special purpose register errors"
summary: "The M-profile file irq_armv7m.S was compiled for an A-profile target, and irq_armv7a.S was built with -mthumb and without FPU flags."
status: "draft"
tool: "cmsis-rtx"
symptoms: ["Error: selected processor does not support requested special purpose register -- `mrseq r0,msp'"]
symptom_regex: "selected\\s+processor\\s+does\\s+not\\s+support\\s+requested\\s+special\\s+purpose\\s+register\\s+\\-\\-\\s+`mrseq\\s+r0,msp'"
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/43"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/43"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-rtx"], "core": ["Cortex-A7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error: selected processor does not support requested special purpose register -- `mrseq r0,msp'`

## Cause

The M-profile file irq_armv7m.S was compiled for an A-profile target, and irq_armv7a.S was built with -mthumb and without FPU flags.

## Fix

Use irq_armv7a.S for Cortex-A, compile it in ARM mode without -mthumb and with proper FPU flags; or use the RTX_Library csolution.

## Source

Resolution: configuration

From [ARM-software/CMSIS-RTX #43](https://github.com/ARM-software/CMSIS-RTX/issues/43), summarized in own words; confidence high, checked against the thread, not reviewed yet.
