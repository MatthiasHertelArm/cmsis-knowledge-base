---
id: "iss-pyocd-743"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32G0 (NUCLEO-G071RB): 'No cores were discovered!' with invalid CoreSight CIDR values"
summary: "On STM32G0 the debug clock is gated until RCC_APBENR1.DBGEN is set, so ROM table reads return garbage after a power cycle; firmware that sets DBGEN (flashed earlier by CubeIDE) hides the problem."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:rom_table:Invalid coresight component, cidr=0x90909090", "CRITICAL:__main__:No cores were discovered!"]
symptom_regex: "Invalid\\s+coresight\\s+component,\\s+cidr=\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/743"
doc_source: "https://github.com/pyocd/pyOCD/issues/743"
resolution: "workaround"
versions: "user scripts need >= 0.22"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32G071RBTx"], "family": ["STM32G0 Series"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:rom_table:Invalid coresight component, cidr=0x90909090`
`CRITICAL:__main__:No cores were discovered!`

## Cause

On STM32G0 the debug clock is gated until RCC_APBENR1.DBGEN is set, so ROM table reads return garbage after a power cycle; firmware that sets DBGEN (flashed earlier by CubeIDE) hides the problem.

## Fix

Use a pyocd user script (`--script`) whose will_init_target hook inserts a task after 'create_aps' that writes the DBGEN bit (address 0x4002103c) before the ROM tables are read; needs a pyOCD version that supports init sequence hooks (newer than 0.21).

## Source

Resolution: workaround

Versions: user scripts need >= 0.22

From [pyocd/pyOCD #743](https://github.com/pyocd/pyOCD/issues/743), summarized in own words; confidence medium, not reviewed yet.
