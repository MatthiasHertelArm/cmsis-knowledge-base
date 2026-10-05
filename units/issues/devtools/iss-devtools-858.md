---
id: "iss-devtools-858"
type: "troubleshooting"
domain: "project"
title: "cbuild: IAR build fails because the preinclude file is passed with -include"
summary: "The IAR toolchain cmake file used the ArmClang option -include for pre-include files after a regression; IAR needs --preinclude."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/858"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/858"
resolution: "fixed-in-release"
versions: "Seen with 1.6 / 1.6.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The IAR toolchain cmake file used the ArmClang option -include for pre-include files after a regression; IAR needs --preinclude.

## Fix

Fixed in the updated IAR toolchain file. As a local patch in IAR.<version>.cmake replace set(_PI "-include") with set(_PI "--preinclude ").

## Source

Resolution: fixed-in-release

Versions: Seen with 1.6 / 1.6.1

From [Open-CMSIS-Pack/devtools #858](https://github.com/Open-CMSIS-Pack/devtools/issues/858), summarized in own words; confidence high, not reviewed yet.
