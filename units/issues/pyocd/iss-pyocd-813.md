---
id: "iss-pyocd-813"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack --install stm32g071rb: 'No matching devices' after failed index downloads"
summary: "cmsis-pack-manager could not fetch the STM32 pdsc files from keil.com (a problem deep in RustLS; curl downloads them fine), so the device was not in the local index."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:__main__:No matching devices. Please make sure the pack index is up to date."]
symptom_regex: "No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/813"
doc_source: "https://github.com/pyocd/pyOCD/issues/813"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32G071RB"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:__main__:No matching devices. Please make sure the pack index is up to date.`

## Cause

cmsis-pack-manager could not fetch the STM32 pdsc files from keil.com (a problem deep in RustLS; curl downloads them fine), so the device was not in the local index.

## Fix

Download the DFP from the Keil CMSIS-Pack list and pass it to pyOCD with --pack. One user still got 'Target type not recognized' with --pack and with a pack: entry in the config file; that stayed open in the thread.

## Source

Resolution: workaround

From [pyocd/pyOCD #813](https://github.com/pyocd/pyOCD/issues/813), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
