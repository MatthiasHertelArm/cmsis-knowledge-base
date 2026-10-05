---
id: "iss-pyocd-1323"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb memory reads on Cortex-M7 return stale data instead of D-cache contents"
summary: "pyOCD reads memory through the MEM-AP with default HPROT 0x3, which ignores the CPU data cache."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1323"
doc_source: "https://github.com/pyocd/pyOCD/issues/1323"
resolution: "configuration"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32H750"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD reads memory through the MEM-AP with default HPROT 0x3, which ignores the CPU data cache. Data in cache not yet cleaned is therefore not visible.

## Fix

Make AP transfers cacheable: monitor set hprot 0xb after connecting (check with monitor show hprot), for cortex-debug in postAttachCommands. In a user script: def did_connect(): target.aps[0].hprot = 0xb.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1323](https://github.com/pyocd/pyOCD/issues/1323), summarized in own words; confidence high, not reviewed yet.
