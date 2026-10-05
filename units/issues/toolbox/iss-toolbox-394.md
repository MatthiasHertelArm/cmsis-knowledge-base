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
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error: L6218E: Undefined symbol osRtxThreadStackCheck (referred from irq_armv7m.o).`

## Cause

No dependency flags were passed for armclang ASM files, so the assembly source had no recorded dependency on RTX_Config.h and was not reassembled after the configuration change.

## Fix

Rebuild the solution as a workaround. The maintainer proposed setting the ASM dependency flags in the AC6 build configuration, and the reporter confirmed that a later toolbox nightly fixes it; no release is named.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cmsis-toolbox #394](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/394), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
