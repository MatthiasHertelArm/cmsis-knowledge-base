---
id: "iss-pyocd-1148"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H743 ROM table probe fails with memory transfer fault on connect"
summary: "The maintainer said this is the same as the STM32L4S5 case: STM32H7 and F7 parts need DBGMCU_CR set to wake the debug domain and keep it awake before CoreSight discovery, otherwise ROM table reads fault."
status: "draft"
tool: "pyocd"
symptoms: ["0000861:WARNING:rom_table:Invalid coresight component, cidr=0x0"]
symptom_regex: "\\S+:WARNING:rom_table:Invalid\\s+coresight\\s+component,\\s+cidr=\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1148"
doc_source: "https://github.com/pyocd/pyOCD/issues/1148"
resolution: "workaround"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H743ZITx"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000861:WARNING:rom_table:Invalid coresight component, cidr=0x0`

## Cause

The maintainer said this is the same as the STM32L4S5 case: STM32H7 and F7 parts need DBGMCU_CR set to wake the debug domain and keep it awake before CoreSight discovery, otherwise ROM table reads fault. This was not confirmed for this board.

## Fix

A pyocd_user.py that writes DBGMCU_CR (0xE00E1004 on H743) through raw AP0 CSW/TAR/DRW writes right after dp_init was suggested, also with value 0x00670007; neither worked for the reporter. pyOCD did connect after STM32CubeIDE had connected first, as long as --connect=under-reset was not used.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1148](https://github.com/pyocd/pyOCD/issues/1148), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
