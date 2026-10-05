---
id: "iss-pyocd-963"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Atmel EDBG CMSIS-DAP probe (SAMC21) not detected since pyocd 0.24"
summary: "Newer pyOCD releases filter CMSIS-DAP probes by name strings, and the Atmel EDBG/Atmel-ICE product names were not matched."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/963"
doc_source: "https://github.com/pyocd/pyOCD/issues/963"
resolution: "fixed-in-release"
versions: "affected 0.24 to 0.27.x"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["ATSAMC21J18A"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Newer pyOCD releases filter CMSIS-DAP probes by name strings, and the Atmel EDBG/Atmel-ICE product names were not matched.

## Fix

Use a release that includes Atmel-ICE/EDBG support (PR #991); pyocd 0.23 detected it as an older workaround.

## Source

Resolution: fixed-in-release

Versions: affected 0.24 to 0.27.x

From [pyocd/pyOCD #963](https://github.com/pyocd/pyOCD/issues/963), summarized in own words; confidence low, not reviewed yet.
