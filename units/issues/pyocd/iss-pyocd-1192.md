---
id: "iss-pyocd-1192"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32L475 built-in target has wrong DBGMCU register addresses"
summary: "A typo in the built-in target put the freeze registers at wrong addresses."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1192"
doc_source: "https://github.com/pyocd/pyOCD/issues/1192"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32L475"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A typo in the built-in target put the freeze registers at wrong addresses.

## Fix

Fixed by change #1193. For other STM32 parts use the CMSIS pack with a user script or debug sequences for DBGMCU.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1192](https://github.com/pyocd/pyOCD/issues/1192), summarized in own words; confidence medium, not reviewed yet.
