---
id: "iss-devtools-1308"
type: "troubleshooting"
domain: "project"
title: "cbuild: CLANG build crashes or cannot find C headers with LLVM 17 for Cortex-M"
summary: "The CLANG toolchain file used an -mfpu option that crashes the compiler, a wrong CLANG_ARCH runtime folder, and explicit -isystem paths that did not find the standard headers."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1308"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1308"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CLANG toolchain file used an -mfpu option that crashes the compiler, a wrong CLANG_ARCH runtime folder, and explicit -isystem paths that did not find the standard headers.

## Fix

Use CMSIS-Toolbox 2.3.0-dev0 or later, confirmed to work with LLVM 17. Before that, the workaround was a CLANG cmake file without -mfpu that uses a sysroot option instead of the -isystem paths.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #1308](https://github.com/Open-CMSIS-Pack/devtools/issues/1308), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
