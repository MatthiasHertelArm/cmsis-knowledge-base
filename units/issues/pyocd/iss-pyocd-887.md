---
id: "iss-pyocd-887"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack install says 'No matching devices' because keil.com pack downloads fail"
summary: "The Rust Reqwest/RusTLS libraries used by cmsis-pack-manager could not download several pdsc files from the Keil server (unexpected end of file), so the index lacked the STM32 packs."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:__main__:No matching devices. Please make sure the pack index is up to date.", "ERRO download of \"https://www.keil.com/pack/Keil.STM32G0xx_DFP.pdsc\" failed: error trying to connect: unexpected end of file"]
symptom_regex: "No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/887"
doc_source: "https://github.com/pyocd/pyOCD/issues/887"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:__main__:No matching devices. Please make sure the pack index is up to date.`
`ERRO download of "https://www.keil.com/pack/Keil.STM32G0xx_DFP.pdsc" failed: error trying to connect: unexpected end of file`

## Cause

The Rust Reqwest/RusTLS libraries used by cmsis-pack-manager could not download several pdsc files from the Keil server (unexpected end of file), so the index lacked the STM32 packs.

## Fix

Download the DFP from the Keil CMSIS-Pack list and pass it with --pack.

## Source

Resolution: workaround

From [pyocd/pyOCD #887](https://github.com/pyocd/pyOCD/issues/887), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
