---
id: "iss-pyocd-189"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: External nRF51 board cannot be flashed through an nRF51-DK running mbed interface firmware"
summary: "The CMSIS-DAP firmware only drives the SWD pins to the on-board nRF51; the Debug Out header is not used."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/189"
doc_source: "https://github.com/pyocd/pyOCD/issues/189"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["nRF51 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CMSIS-DAP firmware only drives the SWD pins to the on-board nRF51; the Debug Out header is not used.

## Fix

No fix in the thread: the CMSIS-DAP firmware would have to detect an external target and switch SWD to Debug Out, and the reporter planned a feature request for it. With the J-Link firmware the external board could be programmed before.

## Source

Resolution: not-a-bug

From [pyocd/pyOCD #189](https://github.com/pyocd/pyOCD/issues/189), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
