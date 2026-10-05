---
id: "iss-pyocd-643"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Target from a downloaded CMSIS-Pack not found: --pack must be given on every pyocd command"
summary: "The pack was only supplied to gdbserver."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd-flashtool: error: argument -t/--target: invalid choice: 'stm32l476rg'"]
symptom_regex: "pyocd\\-flashtool:\\s+error:\\s+argument\\s+\\-t/\\-\\-target:\\s+invalid\\s+choice:\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/643"
doc_source: "https://github.com/pyocd/pyOCD/issues/643"
resolution: "configuration"
versions: "0.20.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32L4 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd-flashtool: error: argument -t/--target: invalid choice: 'stm32l476rg'`

## Cause

The pack was only supplied to gdbserver. Each tool invocation loads packs independently, and the old pyocd-flashtool does not know pack targets at all.

## Fix

Pass `--pack <file>` to every pyocd invocation, or list the packs once under `pack:` in a pyocd.yaml in the working directory, then use the new combined `pyocd` tool (`pyocd flash`, `pyocd gdbserver`).

## Source

Resolution: configuration

Versions: 0.20.0

From [pyocd/pyOCD #643](https://github.com/pyocd/pyOCD/issues/643), summarized in own words; confidence high, not reviewed yet.
