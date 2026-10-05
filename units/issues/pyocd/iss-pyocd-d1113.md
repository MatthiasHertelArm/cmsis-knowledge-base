---
id: "iss-pyocd-d1113"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H750: invalid CoreSight component warnings, memory transfer fault, slow flashing"
summary: "On STM32H7 parts the trace clock is off after reset, so the CoreSight trace components cannot be read and are reported as invalid."
status: "draft"
tool: "pyocd"
symptoms: ["0001679:WARNING:rom_table:Invalid coresight component, cidr=0x0"]
symptom_regex: "\\S+:WARNING:rom_table:Invalid\\s+coresight\\s+component,\\s+cidr=\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1113"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1113"
resolution: "configuration"
versions: "pyOCD 0.30.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32H750"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001679:WARNING:rom_table:Invalid coresight component, cidr=0x0`

## Cause

On STM32H7 parts the trace clock is off after reset, so the CoreSight trace components cannot be read and are reported as invalid. A target made from a pack plus extra memory regions added in a user script can contain overlapping regions, which produces memory transfer faults (a single access crossing a region boundary). Flash speed is limited by the default 1 MHz SWD clock and the pre-programming flash read.

## Fix

In a did_reset() hook of the user script set bit 20 (TRACECLKEN, 0x00100000) in DBGMCU_CR at 0xE00E1004. Check the memory map with: pyocd cmd -c "show map" and remove overlapping regions; mark SDRAM with is_default=False and is_powered_on_boot=False. For speed use a higher SWD frequency (--frequency 10m) and, for development flows, -Osmart_flash=0.

## Source

Resolution: configuration

Versions: pyOCD 0.30.0

From [pyocd/pyOCD discussion 1113](https://github.com/pyocd/pyOCD/discussions/1113), summarized in own words; confidence medium, not reviewed yet.
