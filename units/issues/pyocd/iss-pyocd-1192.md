---
id: "iss-pyocd-1192"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32L475 built-in target has wrong DBGMCU register addresses"
summary: "The built-in STM32L475 target had wrong addresses for the DBGMCU APB1FZR2 and APB2FZR freeze registers."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1192"
doc_source: "https://github.com/pyocd/pyOCD/issues/1192"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32L475"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The built-in STM32L475 target had wrong addresses for the DBGMCU APB1FZR2 and APB2FZR freeze registers.

## Fix

Fixed by change #1193. For other STM32 parts (e.g. L496) use the CMSIS pack target and write DBGMCU registers from a user script (did_connect hook); debug sequence support was only on the maintainer's feature/debug_sequences branch.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1192](https://github.com/pyocd/pyOCD/issues/1192), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
