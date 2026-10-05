---
id: "iss-pyocd-1549"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: SPSDK breaks with pyOCD 0.35.0: DPConnector missing 'dp' argument"
summary: "pyOCD 0.35.0 changed the DPConnector constructor signature, breaking callers (such as NXP SPSDK) that passed only the probe."
status: "draft"
tool: "pyocd"
symptoms: ["Entering into ISP mode failed: DPConnector.__init__() missing 1 required positional argument: 'dp'"]
symptom_regex: "Entering\\s+into\\s+ISP\\s+mode\\s+failed:\\s+DPConnector\\.__init__\\(\\)\\s+missing\\s+\\S+\\s+required\\s+positional\\s+argument:\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1549"
doc_source: "https://github.com/pyocd/pyOCD/issues/1549"
resolution: "workaround"
versions: "0.35.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Entering into ISP mode failed: DPConnector.__init__() missing 1 required positional argument: 'dp'`

## Cause

pyOCD 0.35.0 changed the DPConnector constructor signature, breaking callers (such as NXP SPSDK) that passed only the probe.

## Fix

Pass the debug port explicitly as the second argument (DPConnector(probe, probe.session.board.target.dp)), as done on the SPSDK side; the maintainer said he would find a way to revert the API change.

## Source

Resolution: workaround

Versions: 0.35.0

From [pyocd/pyOCD #1549](https://github.com/pyocd/pyOCD/issues/1549), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
