---
id: "iss-pyocd-1148"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H743 ROM table probe fails with memory transfer fault on connect"
summary: "STM32H7 parts must have the DBGMCU control register set to enable debug clocks and low-power debug before CoreSight discovery."
status: "draft"
tool: "pyocd"
symptoms: ["0000861:WARNING:rom_table:Invalid coresight component, cidr=0x0"]
symptom_regex: "\\S+:WARNING:rom_table:Invalid\\s+coresight\\s+component,\\s+cidr=\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1148"
doc_source: "https://github.com/pyocd/pyOCD/issues/1148"
resolution: "workaround"
versions: "seen with pyOCD 0.30 era builds"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H743ZITx"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000861:WARNING:rom_table:Invalid coresight component, cidr=0x0`

## Cause

STM32H7 parts must have the DBGMCU control register set to enable debug clocks and low-power debug before CoreSight discovery. Without it parts of the debug domain are asleep and the ROM table reads fault.

## Fix

Add a pyocd_user.py (or --script) that writes DBGMCU_CR (0xE00E1004 on H743) through raw AP register writes right after dp_init, as for the L4S5 case. One reporter found it still failed with connect_mode=under-reset, but pyocd connected once STM32CubeIDE had connected first and under-reset was not used, so try both without under-reset.

## Source

Resolution: workaround

Versions: seen with pyOCD 0.30 era builds

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1148](https://github.com/pyocd/pyOCD/issues/1148), summarized in own words; confidence low, not reviewed yet.
