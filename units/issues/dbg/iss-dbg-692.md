---
id: "iss-dbg-692"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Live View / Memory Inspector values freeze while the CPU runs (Zephyr idle with WFI)"
summary: "pyOCD memory cache returns stale values when the target sits in sleep (WFI) in Zephyr idle; reads then do not reach the target."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/692"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/692"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD memory cache returns stale values when the target sits in sleep (WFI) in Zephyr idle; reads then do not reach the target. It shows with CMSIS-DAP and ULINKplus but not with J-Link.

## Fix

Disable the memory cache with -Ocache.enable_memory=false in the pyOCD arguments, or build Zephyr so that it skips WFI while debugging (CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK with a hook returning false).

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #692](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/692), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
