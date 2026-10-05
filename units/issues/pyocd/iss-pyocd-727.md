---
id: "iss-pyocd-727"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32F7/H7/G0 packs not installable: pack download fails, 'No cores discovered'"
summary: "pyOCD's pack index download was too parallel and triggered the DoS protection of the Keil and NXP servers; separately, firmware left on the chip kept pyOCD from connecting reliably."
status: "draft"
tool: "pyocd"
symptoms: ["ERRO download of \"https://www.keil.com/pack/Keil.STM32H7xx_DFP.pdsc\" failed: unexpected end of file"]
symptom_regex: "download\\s+of\\s+\".*?\"\\s+failed:\\s+unexpected\\s+end\\s+of\\s+file"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/727"
doc_source: "https://github.com/pyocd/pyOCD/issues/727"
resolution: "workaround"
versions: "seen 2019, tracked in cmsis-pack-manager"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32F7 Series", "STM32H7 Series", "STM32G0 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERRO download of "https://www.keil.com/pack/Keil.STM32H7xx_DFP.pdsc" failed: unexpected end of file`

## Cause

pyOCD's pack index download was too parallel and triggered the DoS protection of the Keil and NXP servers; separately, firmware left on the chip kept pyOCD from connecting reliably.

## Fix

Download the DFP from the Keil pack list and pass it with `--pack`; update ST-Link firmware and erase flash if connection still fails.

## Source

Resolution: workaround

Versions: seen 2019, tracked in cmsis-pack-manager

From [pyocd/pyOCD #727](https://github.com/pyocd/pyOCD/issues/727), summarized in own words; confidence medium, not reviewed yet.
