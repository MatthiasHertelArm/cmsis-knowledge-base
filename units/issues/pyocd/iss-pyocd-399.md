---
id: "iss-pyocd-399"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd does not list an nRF52 board that only has a J-Link firmware"
summary: "The pyOCD of that time only spoke CMSIS-DAP over USB."
status: "draft"
tool: "pyocd"
symptoms: ["No available boards are connected"]
symptom_regex: "No\\s+available\\s+boards\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/399"
doc_source: "https://github.com/pyocd/pyOCD/issues/399"
resolution: "configuration"
versions: "0.11.x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["nRF52 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available boards are connected`

## Cause

The pyOCD of that time only spoke CMSIS-DAP over USB. A board whose on-board interface runs J-Link firmware is invisible to it.

## Fix

Flash CMSIS-DAP interface firmware to the board's debug MCU (from the vendor) or use a CMSIS-DAP probe; newer pyOCD versions also support J-Link probes.

## Source

Resolution: configuration

Versions: 0.11.x

From [pyocd/pyOCD #399](https://github.com/pyocd/pyOCD/issues/399), summarized in own words; confidence medium, not reviewed yet.
