---
id: "iss-pyocd-1629"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flash algorithm not halting (IPSR=3) when its RAM load address is invalid for the MCU"
summary: "IPSR=3 means the core ended in the HardFault handler while running the flash algorithm init."
status: "draft"
tool: "pyocd"
symptoms: ["C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]"]
symptom_regex: "C\\s+target\\s+was\\s+not\\s+halted\\s+as\\s+expected\\s+after\\s+calling\\s+flash\\s+algorithm\\s+routine\\s+\\(IPSR=\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1629"
doc_source: "https://github.com/pyocd/pyOCD/issues/1629"
resolution: "configuration"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S36"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]`

## Cause

IPSR=3 means the core ended in the HardFault handler while running the flash algorithm init. One user found the cause was that the algorithm was loaded at RAM address 0x20000000, which did not exist in their MCU's memory design, so the init routine crashed. On NXP LPC55S36 revision D1 the same message was reported with a new chip ROM; no fix was found there.

## Fix

Check that the flash algorithm's load address and stack lie in RAM that really exists on the device, and change the algorithm's load address to a valid RAM region.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1629](https://github.com/pyocd/pyOCD/issues/1629), summarized in own words; confidence low, not reviewed yet.
