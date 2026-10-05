---
id: "iss-devtools-397"
type: "troubleshooting"
domain: "project"
title: "cbuild: Breakpoints cannot be set when debugging a cbuild-built .axf in uVision"
summary: "Debug information in the image contains the source paths of the build machine (for example a Linux or WSL path), which uVision cannot find on the debug host, so no line information is usable."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/397"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/397"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Debug information in the image contains the source paths of the build machine (for example a Linux or WSL path), which uVision cannot find on the debug host, so no line information is usable.

## Fix

In uVision enter the SET SRC=<path to the sources> debug command (UNC paths work) so it can locate the sources; also use -gdwarf-4 for assembler files if needed.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/devtools #397](https://github.com/Open-CMSIS-Pack/devtools/issues/397), summarized in own words; confidence high, not reviewed yet.
