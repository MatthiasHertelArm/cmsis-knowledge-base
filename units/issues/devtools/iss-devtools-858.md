---
id: "iss-devtools-858"
type: "troubleshooting"
domain: "project"
title: "cbuild: IAR build fails because the preinclude file is passed with -include"
summary: "The IAR toolchain cmake file used the ArmClang option -include for pre-include files after PR #798 reverted the earlier fix; IAR needs --preinclude."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/858"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/858"
resolution: "workaround"
versions: "csolution 1.6, cbuild 1.6.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The IAR toolchain cmake file used the ArmClang option -include for pre-include files after PR #798 reverted the earlier fix; IAR needs --preinclude.

## Fix

As a local patch in IAR.<version>.cmake replace set(_PI "-include") with set(_PI "--preinclude "). IAR announced to include the correction in a pending toolchain file update; the thread shows no release.

## Source

Resolution: workaround

Versions: csolution 1.6, cbuild 1.6.1

From [Open-CMSIS-Pack/devtools #858](https://github.com/Open-CMSIS-Pack/devtools/issues/858), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
