---
id: "iss-pyocd-1537"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD cannot step off a bkpt instruction compiled into the firmware"
summary: "A BKPT instruction in the code is not managed by pyOCD's breakpoint manager, so removing it does nothing, and resuming or stepping re-executes it forever. gdb cannot remove it either."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1537"
doc_source: "https://github.com/pyocd/pyOCD/issues/1537"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A BKPT instruction in the code is not managed by pyOCD's breakpoint manager, so removing it does nothing, and resuming or stepping re-executes it forever. gdb cannot remove it either.

## Fix

Before resuming, check whether the instruction at PC is a bkpt and skip it: pc = target.read_core_register('pc'); if (target.read16(pc) & 0xff00) == 0xbe00: target.write_core_register('pc', pc + 2). In gdb use set $pc += 2. Native handling in pyOCD was planned.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1537](https://github.com/pyocd/pyOCD/issues/1537), summarized in own words; confidence medium, not reviewed yet.
