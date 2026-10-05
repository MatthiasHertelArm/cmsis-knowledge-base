---
id: "iss-pyocd-963"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Atmel EDBG CMSIS-DAP probe (SAMC21) not detected since pyocd 0.24"
summary: "Since pyocd 0.24.0 the Atmel EDBG CMSIS-DAP probe is not detected (0.23.0 detects it); the maintainer suspected changes to the checks for CMSIS-DAP names."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/963"
doc_source: "https://github.com/pyocd/pyOCD/issues/963"
resolution: "workaround"
versions: "0.27.3 and 0.24.0 affected; 0.23.0 works"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["ATSAMC21J18A"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Since pyocd 0.24.0 the Atmel EDBG CMSIS-DAP probe is not detected (0.23.0 detects it); the maintainer suspected changes to the checks for CMSIS-DAP names.

## Fix

Downgrade to pyocd 0.23.0 (adapting to its older Python API), which detects the probe. A pull request adding Atmel-ICE support (#991) might fix it too; not confirmed.

## Source

Resolution: workaround

Versions: 0.27.3 and 0.24.0 affected; 0.23.0 works

From [pyocd/pyOCD #963](https://github.com/pyocd/pyOCD/issues/963), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
