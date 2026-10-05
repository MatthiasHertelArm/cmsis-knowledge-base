---
id: "iss-devtools-978"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild fails on macOS/Linux: empty cmake.in files missing after vcpkg install"
summary: "The tar extraction used by vcpkg artifacts on macOS and Linux dropped three empty files (CMakeTestAS_ARMCompiler.cmake.in, _GNUCompiler, _LEGCompiler) in the toolbox etc/CMakeASM folder, but cbuild needs them."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/978"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/978"
resolution: "fixed-in-release"
versions: "1.7.0, fixed in 2.0.0-dev2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The tar extraction used by vcpkg artifacts on macOS and Linux dropped three empty files (CMakeTestAS_ARMCompiler.cmake.in, _GNUCompiler, _LEGCompiler) in the toolbox etc/CMakeASM folder, but cbuild needs them.

## Fix

Fixed for CMSIS-Toolbox 2.0.0-dev2 by putting a comment into the files so they are not empty.

## Source

Resolution: fixed-in-release

Versions: 1.7.0, fixed in 2.0.0-dev2

From [Open-CMSIS-Pack/devtools #978](https://github.com/Open-CMSIS-Pack/devtools/issues/978), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
