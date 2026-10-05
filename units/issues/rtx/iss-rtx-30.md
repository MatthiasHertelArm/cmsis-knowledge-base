---
id: "iss-rtx-30"
type: "troubleshooting"
domain: "rtos"
title: "RTX: L6218E undefined osRtxThreadStackCheck after disabling stack overrun checking in uVision"
summary: "The source is correct (guarded by RTX_STACK_CHECK); the IDE did not rebuild the assembler module after RTX_Config.h changed."
status: "draft"
tool: "cmsis-rtx"
symptoms: ["Error: L6218E: Undefined symbol osRtxThreadStackCheck (referred from irq_armv7m.o)."]
symptom_regex: "L6218E:\\s+Undefined\\s+symbol\\s+osRtxThreadStackCheck\\s+\\(referred\\s+from\\s+irq_armv7m\\.o\\)\\."
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/30"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/30"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-rtx"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error: L6218E: Undefined symbol osRtxThreadStackCheck (referred from irq_armv7m.o).`

## Cause

The source is correct (guarded by RTX_STACK_CHECK); the IDE did not rebuild the assembler module after RTX_Config.h changed.

## Fix

Do a full Rebuild.

## Source

Resolution: workaround

From [ARM-software/CMSIS-RTX #30](https://github.com/ARM-software/CMSIS-RTX/issues/30), summarized in own words; confidence high, not reviewed yet.
