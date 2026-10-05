---
id: "iss-pyocd-1202"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Microchip nEDBG: 'DAP_CONNECT failed' with default protocol"
summary: "The nEDBG probe did not respond properly to the default port selection."
status: "draft"
tool: "pyocd"
symptoms: ["DAP_CONNECT failed"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1202"
doc_source: "https://github.com/pyocd/pyOCD/issues/1202"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DAP_CONNECT failed`

## Cause

The nEDBG probe did not respond properly to the default port selection.

## Fix

Connect with -O dap_protocol=swd. The device identity (variant) selected may also matter for actual programming.

## Source

Resolution: workaround

From [pyocd/pyOCD #1202](https://github.com/pyocd/pyOCD/issues/1202), summarized in own words; confidence low, checked against the thread, not reviewed yet.
