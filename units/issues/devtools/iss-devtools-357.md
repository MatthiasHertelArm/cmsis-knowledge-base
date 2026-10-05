---
id: "iss-devtools-357"
type: "troubleshooting"
domain: "project"
title: "cbuild: AC6 build tries to use /usr/bin/ld as linker on Linux"
summary: "CMake chooses the linker itself; the maintainer named a dirty CMake cache from an earlier misconfigured run as the likely reason the system /usr/bin/ld was picked instead of armlink, which was not confirmed."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/357"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/357"
resolution: "workaround"
versions: "AC6 6.18.0 toolchain file, CMake 3.22.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMake chooses the linker itself; the maintainer named a dirty CMake cache from an earlier misconfigured run as the likely reason the system /usr/bin/ld was picked instead of armlink, which was not confirmed.

## Fix

Set CMAKE_LINKER to the armlink path in the AC6.<version>.cmake toolchain file (confirmed by the reporter), or set LD to ${TOOLCHAIN_ROOT}/armlink${EXT}; cleaning the CMake cache with cbuild <project>.cprj --clear was suggested but not tested.

## Source

Resolution: workaround

Versions: AC6 6.18.0 toolchain file, CMake 3.22.1

From [Open-CMSIS-Pack/devtools #357](https://github.com/Open-CMSIS-Pack/devtools/issues/357), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
