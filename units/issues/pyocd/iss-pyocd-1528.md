---
id: "iss-pyocd-1528"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb cannot read SCB or peripheral registers through pyocd gdbserver"
summary: "gdb by default restricts memory access to the memory map the server supplies."
status: "draft"
tool: "pyocd"
symptoms: ["Cannot access memory at address 0xe000ed00"]
symptom_regex: "Cannot\\s+access\\s+memory\\s+at\\s+address\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1528"
doc_source: "https://github.com/pyocd/pyOCD/issues/1528"
resolution: "configuration"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52840"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Cannot access memory at address 0xe000ed00`

## Cause

gdb by default restricts memory access to the memory map the server supplies. CMSIS-Pack memory maps normally list only flash and RAM, not device regions such as the peripheral area or PPB, so gdb refuses those reads.

## Fix

Tell gdb to ignore the supplied map: set mem inaccessible-by-default no. Invalid accesses then simply fault on the target. Alternatively add DeviceRegion entries for Peripheral and PPB in a user script's will_connect.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1528](https://github.com/pyocd/pyOCD/issues/1528), summarized in own words; confidence high, not reviewed yet.
