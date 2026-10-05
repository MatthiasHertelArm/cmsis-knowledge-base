---
id: "iss-pyocd-887"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack install says 'No matching devices' because keil.com pack downloads fail"
summary: "The pack manager's Rust TLS stack could not download several pdsc files from the Keil server (unexpected end of file), so the index lacked the STM32 packs."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:__main__:No matching devices. Please make sure the pack index is up to date.", "ERRO download of \"https://www.keil.com/pack/Keil.STM32G0xx_DFP.pdsc\" failed: error trying to connect: unexpected end of file"]
symptom_regex: "No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/887"
doc_source: "https://github.com/pyocd/pyOCD/issues/887"
resolution: "workaround"
versions: "seen 2020 with 0.26-0.27"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:__main__:No matching devices. Please make sure the pack index is up to date.`
`ERRO download of "https://www.keil.com/pack/Keil.STM32G0xx_DFP.pdsc" failed: error trying to connect: unexpected end of file`

## Cause

The pack manager's Rust TLS stack could not download several pdsc files from the Keil server (unexpected end of file), so the index lacked the STM32 packs.

## Fix

Download the DFP from the Keil pack list and pass it with `--pack <file.pack>`.

## Source

Resolution: workaround

Versions: seen 2020 with 0.26-0.27

From [pyocd/pyOCD #887](https://github.com/pyocd/pyOCD/issues/887), summarized in own words; confidence high, not reviewed yet.
