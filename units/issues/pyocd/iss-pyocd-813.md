---
id: "iss-pyocd-813"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack --install stm32g071rb: 'No matching devices' after failed index downloads"
summary: "The pack manager could not fetch the STM32 pdsc files from keil.com (a TLS library problem), so the device was not in the local index."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:__main__:No matching devices. Please make sure the pack index is up to date."]
symptom_regex: "No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/813"
doc_source: "https://github.com/pyocd/pyOCD/issues/813"
resolution: "workaround"
versions: "seen early 2020"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32G071RB"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:__main__:No matching devices. Please make sure the pack index is up to date.`

## Cause

The pack manager could not fetch the STM32 pdsc files from keil.com (a TLS library problem), so the device was not in the local index.

## Fix

Download the DFP manually and use `--pack`; check with `pyocd list --targets --pack <file>`. Later versions of pyOCD and cmsis-pack-manager fixed the download.

## Source

Resolution: workaround

Versions: seen early 2020

From [pyocd/pyOCD #813](https://github.com/pyocd/pyOCD/issues/813), summarized in own words; confidence medium, not reviewed yet.
