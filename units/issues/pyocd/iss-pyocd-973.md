---
id: "iss-pyocd-973"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 'No ACK received' on the first access to an nRF52840 board"
summary: "No response at all to the first SWD read; the maintainer says this most often means the MCU is asleep in a low-power mode (WFI/WFE) that disables debug, and the default Mbed build neither enables debug nor disables sleep …"
status: "draft"
tool: "pyocd"
symptoms: ["CRITICAL:__main__:No ACK received"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/973"
doc_source: "https://github.com/pyocd/pyOCD/issues/973"
resolution: "unresolved"
versions: "0.28.1, 0.28.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["nRF52840"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CRITICAL:__main__:No ACK received`

## Cause

No response at all to the first SWD read; the maintainer says this most often means the MCU is asleep in a low-power mode (WFI/WFE) that disables debug, and the default Mbed build neither enables debug nor disables sleep on idle.

## Fix

Build with the Mbed debug profile so debug stays enabled and automatic sleep is off. --connect=under-reset did not help because the nRF52840 does not expose nRESET on a pin unless UICR.PSELRESET is programmed; otherwise try to connect while the firmware is awake or as the MCU powers on.

## Source

Resolution: unresolved

Versions: 0.28.1, 0.28.2

From [pyocd/pyOCD #973](https://github.com/pyocd/pyOCD/issues/973), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
