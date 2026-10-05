---
id: "iss-pyocd-d1380"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Target type mimxrt1160_cm7 not recognized when flashing with west -r pyocd"
summary: "The board ID table maps the RT1160 EVK to a target type that does not exist as a built-in target; it was a mistake in the table."
status: "draft"
tool: "pyocd"
symptoms: ["0023806 C Target type mimxrt1160_cm7 not recognized. Use 'pyocd list --targets' to see currently available target types.", "pyocd.core.exceptions.TargetSupportError: Target type mimxrt1160_cm7 not recognized."]
symptom_regex: "Target\\s+type\\s+mimxrt1160_cm7\\s+not\\s+recognized\\.\\s+Use\\s+'.*?'\\s+to\\s+see\\s+currently\\s+available\\s+target\\s+types\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1380"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1380"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT1166"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0023806 C Target type mimxrt1160_cm7 not recognized. Use 'pyocd list --targets' to see currently available target types.`
`pyocd.core.exceptions.TargetSupportError: Target type mimxrt1160_cm7 not recognized.`

## Cause

The board ID table maps the RT1160 EVK to a target type that does not exist as a built-in target; it was a mistake in the table.

## Fix

Install the device through its CMSIS-Pack as described in the target support documentation and select that target, or try the built-in mimxrt1170_cm7 target.

## Source

Resolution: workaround

From [pyocd/pyOCD discussion 1380](https://github.com/pyocd/pyOCD/discussions/1380), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
