---
id: "iss-pyocd-1695"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: target was not halted as expected after calling flash algorithm routine since pyOCD 0.36"
summary: "Starting with the 0.36 series the halt-after-reset sequence is unreliable on several pack-based targets (HK32, STM32L0, Nuvoton, NXP MCX): the core sometimes keeps running, so the flash algorithm cannot start."
status: "draft"
tool: "pyocd"
symptoms: ["C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]", "W Timed out waiting for core to halt after reset (state is RUNNING) [cortex_m]"]
symptom_regex: "C\\s+target\\s+was\\s+not\\s+halted\\s+as\\s+expected\\s+after\\s+calling\\s+flash\\s+algorithm\\s+routine\\s+\\(IPSR=\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1695"
doc_source: "https://github.com/pyocd/pyOCD/issues/1695"
resolution: "workaround"
versions: "Regression from 0.36.0; still seen in 0.41 and 0.44.1; 0.35.1 works."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]`
`W Timed out waiting for core to halt after reset (state is RUNNING) [cortex_m]`

## Cause

Starting with the 0.36 series the halt-after-reset sequence is unreliable on several pack-based targets (HK32, STM32L0, Nuvoton, NXP MCX): the core sometimes keeps running, so the flash algorithm cannot start. The thread has no root cause; it affects 0.41 and 0.44.1 too.

## Fix

Install pyOCD 0.35.1 (pip install pyocd==0.35.1), which works on the same hardware. For NXP MCX boards under Zephyr, west flash -r linkserver avoids the problem. Tuning connect mode and reset timing did not make the failure reliable.

## Source

Resolution: workaround

Versions: Regression from 0.36.0; still seen in 0.41 and 0.44.1; 0.35.1 works.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1695](https://github.com/pyocd/pyOCD/issues/1695), summarized in own words; confidence medium, not reviewed yet.
