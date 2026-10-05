---
id: "iss-pyocd-624"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb 'load' fails and warns about missing <memory> element: target is the generic cortex_m"
summary: "No target type was set, so pyOCD used the generic cortex_m target."
status: "draft"
tool: "pyocd"
symptoms: ["warning: while parsing target memory map (at line 3): Required element <memory> is missing"]
symptom_regex: "while\\s+parsing\\s+target\\s+memory\\s+map\\s+\\(at\\s+line\\s+\\S+\\):\\s+Required\\s+element\\s+<memory>\\s+is\\s+missing"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/624"
doc_source: "https://github.com/pyocd/pyOCD/issues/624"
resolution: "configuration"
versions: "0.19.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32F1 Series", "STM32F4 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning: while parsing target memory map (at line 3): Required element <memory> is missing`

## Cause

No target type was set, so pyOCD used the generic cortex_m target. It provides no memory map and no flash algorithm, hence gdb complains and cannot load. STLink probes were not auto-detected at that time.

## Fix

Obtain the device pack (or use a release with pack support), then start with `--pack <file> -t <device>`, for example `pyocd gdbserver --pack <Keil.STM32F1xx_DFP>.pack -t stm32f103ze`. The pack subcommand only exists from 0.20.0.

## Source

Resolution: configuration

Versions: 0.19.0

From [pyocd/pyOCD #624](https://github.com/pyocd/pyOCD/issues/624), summarized in own words; confidence high, not reviewed yet.
