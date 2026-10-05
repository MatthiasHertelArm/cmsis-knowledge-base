---
id: "iss-pyocd-1700"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H7 flash corrupted occasionally with double buffering"
summary: "Double-buffered flash programming can stall on the bus of devices with strict timing such as STM32H7, leaving pages partly written (rest 0xFF) without any error."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1700"
doc_source: "https://github.com/pyocd/pyOCD/issues/1700"
resolution: "fixed-in-release"
versions: "v0.38.0 named as the latest release with the change"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32H750VBTx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Double-buffered flash programming can stall on the bus of devices with strict timing such as STM32H7, leaving pages partly written (rest 0xFF) without any error.

## Fix

Upgrade to a current pyOCD (v0.38.0 when the issue was closed), which disables double buffering for flash algorithms by default. A built-in stm32h743xx target adapted to the H750 flash layout also programmed reliably, unlike the pack's flash loader.

## Source

Resolution: fixed-in-release

Versions: v0.38.0 named as the latest release with the change

From [pyocd/pyOCD #1700](https://github.com/pyocd/pyOCD/issues/1700), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
