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
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMake falls back to a gcc from PATH if the compiler is not registered.

## Fix

Register the compiler with the environment variable GCC_TOOLCHAIN_<major>_<minor>_<patch> holding the absolute path to its bin directory (Toolchain Registration); another user fixed it by correcting the path and environment variables.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/cmsis-toolbox #95](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/95), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
