---
id: "iss-toolbox-95"
type: "troubleshooting"
domain: "project"
title: "csolution: Wrong GCC picked when several GCC toolchains are on PATH"
summary: "CMake falls back to a gcc from PATH if the compiler is not registered."
status: "draft"
tool: "csolution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/95"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/95"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMake falls back to a gcc from PATH if the compiler is not registered.

## Fix

Register the compiler with an environment variable such as GCC_TOOLCHAIN_<major>_<minor>_<patch> pointing to its bin folder, and verify with cbuild list toolchains.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/cmsis-toolbox #95](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/95), summarized in own words; confidence high, not reviewed yet.
