---
id: "iss-devtools-357"
type: "troubleshooting"
domain: "project"
title: "cbuild: AC6 build tries to use /usr/bin/ld as linker on Linux"
summary: "CMake chooses the linker itself; picking the system ld although armlink is the compiler's linker is a symptom of a stale CMake cache from an earlier misconfigured run."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/357"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/357"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMake chooses the linker itself; picking the system ld although armlink is the compiler's linker is a symptom of a stale CMake cache from an earlier misconfigured run.

## Fix

Clean the CMake cache with cbuild <project>.cprj --clear; as a workaround set CMAKE_LINKER to the armlink path in the AC6.<version>.cmake toolchain file.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #357](https://github.com/Open-CMSIS-Pack/devtools/issues/357), summarized in own words; confidence medium, not reviewed yet.
