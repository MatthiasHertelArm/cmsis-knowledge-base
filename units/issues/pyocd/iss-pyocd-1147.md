---
id: "iss-pyocd-1147"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32L4S5 'DP wait' or invalid CoreSight IDs when firmware uses deep sleep"
summary: "The firmware enters a low-power mode (Mbed sleep_for puts the MCU into Stop2)."
status: "draft"
tool: "pyocd"
symptoms: ["STLink error (20): DP wait"]
symptom_regex: "STLink\\s+error\\s+\\(\\S+\\):\\s+DP\\s+wait"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1147"
doc_source: "https://github.com/pyocd/pyOCD/issues/1147"
resolution: "workaround"
versions: "pyOCD 0.30.3 and earlier"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32L4 Series"], "device": ["STM32L4S5VITx"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`STLink error (20): DP wait`

## Cause

The firmware enters a low-power mode (Mbed sleep_for puts the MCU into Stop2). Recent STM32 parts need the DBGMCU_CR debug bits set to wake the debug domain before discovery, so ROM table reads return invalid IDs and the probe reports errors.

## Fix

Put a pyocd_user.py in the working directory (or pass --script) whose will_init_target hook inserts a step after dp_init that writes DBGMCU_CR (0xE0042004 on L4) via AP0 CSW/TAR/DRW writes with value 0x00700007. Confirmed to fix debugging in pyocd and Mbed Studio. Alternatively avoid sleep in debug builds (use wait_us instead of sleep_for). Built-in handling was planned via CMSIS-Pack debug sequences.

## Source

Resolution: workaround

Versions: pyOCD 0.30.3 and earlier

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1147](https://github.com/pyocd/pyOCD/issues/1147), summarized in own words; confidence high, not reviewed yet.
