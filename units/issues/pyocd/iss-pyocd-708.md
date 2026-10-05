---
id: "iss-pyocd-708"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Sector-erase flashing of STM32F091 leaves a 1 KB hole in flash"
summary: "The CMSIS-Pack flash algorithm in the old Keil STM32F0xx DFP declared a 1024-byte sector size while the device uses 2048-byte pages, so the smart flash code programmed only half of each page."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/708"
doc_source: "https://github.com/pyocd/pyOCD/issues/708"
resolution: "fixed-in-release"
versions: "fixed in DFP 2.1.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32F091RC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CMSIS-Pack flash algorithm in the old Keil STM32F0xx DFP declared a 1024-byte sector size while the device uses 2048-byte pages, so the smart flash code programmed only half of each page.

## Fix

Use Keil.STM32F0xx_DFP 2.1.0 or newer, which corrects the sector size.

## Source

Resolution: fixed-in-release

Versions: fixed in DFP 2.1.0

From [pyocd/pyOCD #708](https://github.com/pyocd/pyOCD/issues/708), summarized in own words; confidence high, not reviewed yet.
