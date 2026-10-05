---
id: "iss-toolbox-394"
type: "troubleshooting"
domain: "project"
title: "cbuild: Undefined symbol osRtxThreadStackCheck after turning off RTX stack overrun checking"
summary: "No dependency flags were passed for armclang ASM files, so the assembly source had no recorded dependency on RTX_Config.h and was not reassembled after the configuration change."
status: "draft"
tool: "cbuild"
symptoms: ["Error: L6218E: Undefined symbol osRtxThreadStackCheck (referred from irq_armv7m.o)."]
symptom_regex: "L6218E:\\s+Undefined\\s+symbol\\s+osRtxThreadStackCheck\\s+\\(referred\\s+from\\s+irq_armv7m\\.o\\)\\."
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/394"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/394"
resolution: "fixed-in-release"
versions: "before July 2025 nightlies"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error: L6218E: Undefined symbol osRtxThreadStackCheck (referred from irq_armv7m.o).`

## Cause

No dependency flags were passed for armclang ASM files, so the assembly source had no recorded dependency on RTX_Config.h and was not reassembled after the configuration change.

## Fix

Rebuild the solution as a workaround. Fixed by adding dependency flags for AC6 assembler files in the toolbox nightly of mid July 2025.

## Source

Resolution: fixed-in-release

Versions: before July 2025 nightlies

From [Open-CMSIS-Pack/cmsis-toolbox #394](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/394), summarized in own words; confidence high, not reviewed yet.
