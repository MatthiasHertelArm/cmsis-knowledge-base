---
id: "iss-devtools-667"
type: "troubleshooting"
domain: "project"
title: "csolution: IAR linker script .icf is converted to category other and the link fails"
summary: "The .icf extension was not recognized as a linker script, so the cprj entry got category other."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/667"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/667"
resolution: "fixed-in-release"
versions: "fixed in 1.5.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The .icf extension was not recognized as a linker script, so the cprj entry got category other.

## Fix

Fixed in CMSIS-Toolbox 1.5.0, which recognizes .icf as a linker script.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.5.0

From [Open-CMSIS-Pack/devtools #667](https://github.com/Open-CMSIS-Pack/devtools/issues/667), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
