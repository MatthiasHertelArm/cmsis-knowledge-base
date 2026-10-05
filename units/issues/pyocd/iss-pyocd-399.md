---
id: "iss-pyocd-399"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd does not list an nRF52 board that only has a J-Link firmware"
summary: "pyOCD at that time supported only the CMSIS-DAP protocol."
status: "draft"
tool: "pyocd"
symptoms: ["No available boards are connected"]
symptom_regex: "No\\s+available\\s+boards\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/399"
doc_source: "https://github.com/pyocd/pyOCD/issues/399"
resolution: "configuration"
versions: "0.11.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["nRF52 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available boards are connected`

## Cause

pyOCD at that time supported only the CMSIS-DAP protocol. A board whose interface runs J-Link firmware is invisible to it.

## Fix

Install the CMSIS-DAP interface firmware from Nordic on the board's interface MCU; pyOCD then sees the board.

## Source

Resolution: configuration

Versions: 0.11.2

From [pyocd/pyOCD #399](https://github.com/pyocd/pyOCD/issues/399), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
