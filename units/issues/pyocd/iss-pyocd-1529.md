---
id: "iss-pyocd-1529"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PyInstaller-built pyOCD app fails to open ST-Link session or lacks probes, targets"
summary: "pyOCD loads its probe drivers and RTOS plug-ins through package entry points, which PyInstaller does not collect by default, so the frozen app lacks them."
status: "draft"
tool: "pyocd"
symptoms: ["AssertionError", "Target type stm32l431vctx not recognized. Use 'pyocd list --targets' to see currently available target types."]
symptom_regex: "Target\\s+type\\s+stm32l431vctx\\s+not\\s+recognized\\.\\s+Use\\s+'.*?'\\s+to\\s+see\\s+currently\\s+available\\s+target\\s+types\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1529"
doc_source: "https://github.com/pyocd/pyOCD/issues/1529"
resolution: "workaround"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`AssertionError`
`Target type stm32l431vctx not recognized. Use 'pyocd list --targets' to see currently available target types.`

## Cause

pyOCD loads its probe drivers and RTOS plug-ins through package entry points, which PyInstaller does not collect by default, so the frozen app lacks them.

## Fix

In the .spec file use collect_entry_point('pyocd.probe') and collect_entry_point('pyocd.rtos') from PyInstaller.utils.hooks and add their datas and hidden imports. Also bundle the pyocd package folder as data and keep the _internal folder with the executable. A later 'target type not recognized' error with this setup stayed unresolved.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1529](https://github.com/pyocd/pyOCD/issues/1529), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
