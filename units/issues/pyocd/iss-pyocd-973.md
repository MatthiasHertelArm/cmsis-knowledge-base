---
id: "iss-pyocd-973"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 'No ACK received' on the first access to an nRF52840 board"
summary: "No response at all to the first SWD read means the MCU is not answering debug requests, most often because firmware put it into a sleep mode (WFI/WFE) that powers down debug; the default Mbed build profile does not …"
status: "draft"
tool: "pyocd"
symptoms: ["CRITICAL:__main__:No ACK received"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/973"
doc_source: "https://github.com/pyocd/pyOCD/issues/973"
resolution: "configuration"
versions: "seen with 0.28.x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52840"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CRITICAL:__main__:No ACK received`

## Cause

No response at all to the first SWD read means the MCU is not answering debug requests, most often because firmware put it into a sleep mode (WFI/WFE) that powers down debug; the default Mbed build profile does not keep debug alive.

## Fix

Build with the debug profile so sleep is disabled, try `--connect=under-reset` if the reset line is wired, or reset the part so it wakes before connecting.

## Source

Resolution: configuration

Versions: seen with 0.28.x

From [pyocd/pyOCD #973](https://github.com/pyocd/pyOCD/issues/973), summarized in own words; confidence medium, not reviewed yet.
