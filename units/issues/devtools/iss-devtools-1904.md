---
id: "iss-devtools-1904"
type: "troubleshooting"
domain: "project"
title: "cbuild: CLANG 19 fails to compile for Armv8.1-M with --target=armv8.1m.main-none-unknown-eabihf"
summary: "LLVM Embedded Toolchain 19.1.1 expects target triples starting with thumbv7m, thumbv8m, thumbv8.1m instead of armv7m, armv8m, armv8.1m, which the CLANG toolchain file of the toolbox used."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1904"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1904"
resolution: "fixed-in-release"
versions: "LLVM 19.1.1 with toolbox before 2.7.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"], "core": ["Cortex-M55"], "toolchain": ["CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

LLVM Embedded Toolchain 19.1.1 expects target triples starting with thumbv7m, thumbv8m, thumbv8.1m instead of armv7m, armv8m, armv8.1m, which the CLANG toolchain file of the toolbox used.

## Fix

Fixed in the CLANG cmake file of CMSIS-Toolbox 2.7.0; update the toolbox. Before that the file CLANG.17.0.1.cmake in the toolbox etc folder could be replaced by the one from devtools main.

## Source

Resolution: fixed-in-release

Versions: LLVM 19.1.1 with toolbox before 2.7.0

From [Open-CMSIS-Pack/devtools #1904](https://github.com/Open-CMSIS-Pack/devtools/issues/1904), summarized in own words; confidence high, checked against the thread, not reviewed yet.
