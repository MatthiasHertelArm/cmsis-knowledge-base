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
versions: "2.2.x, fixed in 2.3.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CLANG toolchain file used an -mfpu option that crashes the compiler, a wrong CLANG_ARCH runtime folder, and explicit -isystem paths that did not find the standard headers.

## Fix

Fixed in CMSIS-Toolbox 2.3.0 (confirmed with 2.3.0-dev0): the CLANG cmake file drops -mfpu and uses sysroot so the compiler finds its runtime.

## Source

Resolution: fixed-in-release

Versions: 2.2.x, fixed in 2.3.0

From [Open-CMSIS-Pack/devtools #1308](https://github.com/Open-CMSIS-Pack/devtools/issues/1308), summarized in own words; confidence high, not reviewed yet.
