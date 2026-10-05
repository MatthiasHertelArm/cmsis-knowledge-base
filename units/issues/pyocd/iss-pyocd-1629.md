---
id: "iss-pyocd-1629"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flash algorithm not halting (IPSR=3) when its RAM load address is invalid for the MCU"
summary: "The flash algorithm did not reach its expected halt."
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
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S36"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]`

## Cause

The flash algorithm did not reach its expected halt. For one user with another chip the algorithm was loaded at 0x20000000, which is not valid memory on that MCU, so its init routine did not run correctly. For the LPC55S36 RevD1 board in the report the reporter suspected changes in the new chip ROM; that case stayed unsolved.

## Fix

Check that the flash algorithm is loaded into RAM that exists on the device and move its load address if not; that fixed it for the other user.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1629](https://github.com/pyocd/pyOCD/issues/1629), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
