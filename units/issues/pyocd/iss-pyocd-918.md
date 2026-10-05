---
id: "iss-pyocd-918"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing an nRF52 via ST-LINK V2 fails with 'STLink error (29)' after a tool update"
summary: "ST-Link firmware V2J37S7 apparently refuses to work with non-STM32 devices (the maintainer's belief); with V2J34S7 the nRF52832 could be flashed again."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/918"
doc_source: "https://github.com/pyocd/pyOCD/issues/918"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["nRF52832"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

ST-Link firmware V2J37S7 apparently refuses to work with non-STM32 devices (the maintainer's belief); with V2J34S7 the nRF52832 could be flashed again.

## Fix

Downgrade the ST-Link firmware to an older version such as V2J34S7.

## Source

Resolution: workaround

From [pyocd/pyOCD #918](https://github.com/pyocd/pyOCD/issues/918), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
