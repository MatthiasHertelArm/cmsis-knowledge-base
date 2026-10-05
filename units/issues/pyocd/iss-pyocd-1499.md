---
id: "iss-pyocd-1499"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Board ID maps to a target name pyOCD does not recognise (stm32h745zihx)"
summary: "The board ID table appears to assign a wrong target name (stm32h745zihx) to the DISCO-H745I board."
status: "draft"
tool: "pyocd"
symptoms: ["Target type stm32h745zihx not recognized. Use 'pyocd list --targets' to see currently available target types."]
symptom_regex: "Target\\s+type\\s+stm32h745zihx\\s+not\\s+recognized\\.\\s+Use\\s+'.*?'\\s+to\\s+see\\s+currently\\s+available\\s+target\\s+types\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1499"
doc_source: "https://github.com/pyocd/pyOCD/issues/1499"
resolution: "workaround"
versions: "Keil.STM32H7xx_DFP 3.0.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32H745XIHx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Target type stm32h745zihx not recognized. Use 'pyocd list --targets' to see currently available target types.`

## Cause

The board ID table appears to assign a wrong target name (stm32h745zihx) to the DISCO-H745I board.

## Fix

Pass the right target explicitly, e.g. -t STM32H745XIHx. Flash loading then still failed (flash algorithm not halted, IPSR=3) and the thread leaves that open.

## Source

Resolution: workaround

Versions: Keil.STM32H7xx_DFP 3.0.0

From [pyocd/pyOCD #1499](https://github.com/pyocd/pyOCD/issues/1499), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
