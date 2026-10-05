---
id: "iss-pyocd-918"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing an nRF52 via ST-LINK V2 fails with 'STLink error (29)' after a tool update"
summary: "ST-LINK firmware versions (V2J37S7 in this case) refuse to operate on non-STM32 targets; the earlier firmware worked."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/918"
doc_source: "https://github.com/pyocd/pyOCD/issues/918"
resolution: "workaround"
versions: "seen July 2020"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52832"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

ST-LINK firmware versions (V2J37S7 in this case) refuse to operate on non-STM32 targets; the earlier firmware worked.

## Fix

Flash an older ST-LINK firmware such as V2J34S7, or use a CMSIS-DAP/J-Link probe for non-ST targets.

## Source

Resolution: workaround

Versions: seen July 2020

From [pyocd/pyOCD #918](https://github.com/pyocd/pyOCD/issues/918), summarized in own words; confidence medium, not reviewed yet.
