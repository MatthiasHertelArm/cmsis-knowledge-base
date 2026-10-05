---
id: "iss-devtools-2314"
type: "troubleshooting"
domain: "general"
title: "other: ExecuTorch with Clang embedded toolchain lacks std::chrono::steady_clock and random_device"
summary: "The libc++ shipped with the Clang-based embedded toolchain has no monotonic clock or entropy source implementation for bare metal, so ExecuTorch code using them does not compile or link."
status: "draft"
tool: "other"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2314"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2314"
resolution: "workaround"
versions: "ATfE 21.1.1"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["other"], "toolchain": ["Clang"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The libc++ shipped with the Clang-based embedded toolchain has no monotonic clock or entropy source implementation for bare metal, so ExecuTorch code using them does not compile or link.

## Fix

Provide the missing pieces through stub implementations (the CMSIS-Executorch project ships a posix stub source for this) and use a Clang toolchain file equivalent to the GCC one. A temporary alternative in the thread was to take libstdc++ from a GCC installation.

## Source

Resolution: workaround

Versions: ATfE 21.1.1

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2314](https://github.com/Open-CMSIS-Pack/devtools/issues/2314), summarized in own words; confidence low, checked against the thread, not reviewed yet.
