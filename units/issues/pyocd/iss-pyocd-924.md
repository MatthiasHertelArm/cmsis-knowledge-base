---
id: "iss-pyocd-924"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing with '-t cortex_m' programs 0 bytes: no memory region defined"
summary: "The generic cortex_m target has no memory map or flash algorithm, so there is nowhere to program."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:file_programmer:Failed to add data chunk: no memory region defined for address 0x08000000"]
symptom_regex: "Failed\\s+to\\s+add\\s+data\\s+chunk:\\s+no\\s+memory\\s+region\\s+defined\\s+for\\s+address\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/924"
doc_source: "https://github.com/pyocd/pyOCD/issues/924"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:file_programmer:Failed to add data chunk: no memory region defined for address 0x08000000`

## Cause

The generic cortex_m target has no memory map or flash algorithm, so there is nowhere to program.

## Fix

Select the real device with -t, using a name from the pack given in the config (`pyocd list --targets --config <cfg> --name <part>`).

## Source

Resolution: user-error

From [pyocd/pyOCD #924](https://github.com/pyocd/pyOCD/issues/924), summarized in own words; confidence high, not reviewed yet.
