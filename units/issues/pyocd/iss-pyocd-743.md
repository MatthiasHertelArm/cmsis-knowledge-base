---
id: "iss-pyocd-743"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32G0 (NUCLEO-G071RB): 'No cores were discovered!' with invalid CoreSight CIDR values"
summary: "The maintainer suspected, from the debug sequences of the STM32G0 pack, that RCC_APBENR1.DBGEN must be set to clock the debug resources before the ROM tables are read; flashing with STM32CubeIDE probably leaves it set, which would explain why the …"
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:rom_table:Invalid coresight component, cidr=0x90909090", "CRITICAL:__main__:No cores were discovered!"]
symptom_regex: "Invalid\\s+coresight\\s+component,\\s+cidr=\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/743"
doc_source: "https://github.com/pyocd/pyOCD/issues/743"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["STM32G071RBTx"], "family": ["STM32G0 Series"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:rom_table:Invalid coresight component, cidr=0x90909090`
`CRITICAL:__main__:No cores were discovered!`

## Cause

The maintainer suspected, from the debug sequences of the STM32G0 pack, that RCC_APBENR1.DBGEN must be set to clock the debug resources before the ROM tables are read; flashing with STM32CubeIDE probably leaves it set, which would explain why the error disappears after flashing that way.

## Fix

Proposed, not confirmed: a pyocd_user.py whose will_init_target hook inserts a task after 'create_aps' that writes 0x08000000 to 0x4002103c. On pyOCD 0.21.0 the parameter had to be named init_sequence, and the script then still failed with a NoneType error.

## Source

Resolution: workaround

From [pyocd/pyOCD #743](https://github.com/pyocd/pyOCD/issues/743), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
