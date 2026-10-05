---
id: "iss-devtools-684"
type: "troubleshooting"
domain: "project"
title: "cbuild: Assembly file with .S extension is not compiled with IAR and CMake 3.21"
summary: "CMake 3.21.x does not treat .S as an assembler source for the IAR toolchain; CMake 3.25 does."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/684"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/684"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMake 3.21.x does not treat .S as an assembler source for the IAR toolchain; CMake 3.25 does.

## Fix

Use CMake 3.25 or newer (a bump of the minimum for IAR was suggested), and make sure the assembler source uses IAR syntax, since GNU-style assembler files do not build with the IAR assembler.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #684](https://github.com/Open-CMSIS-Pack/devtools/issues/684), summarized in own words; confidence medium, not reviewed yet.
