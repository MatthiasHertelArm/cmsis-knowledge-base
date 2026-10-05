---
id: "iss-pyocd-1549"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: SPSDK breaks with pyOCD 0.35.0: DPConnector missing 'dp' argument"
summary: "pyOCD 0.35.0 changed the DPConnector constructor signature, breaking callers that passed only the probe."
status: "draft"
tool: "pyocd"
symptoms: ["Entering into ISP mode failed: DPConnector.__init__() missing 1 required positional argument: 'dp'"]
symptom_regex: "Entering\\s+into\\s+ISP\\s+mode\\s+failed:\\s+DPConnector\\.__init__\\(\\)\\s+missing\\s+\\S+\\s+required\\s+positional\\s+argument:\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1549"
doc_source: "https://github.com/pyocd/pyOCD/issues/1549"
resolution: "fixed-in-release"
versions: "0.35.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Entering into ISP mode failed: DPConnector.__init__() missing 1 required positional argument: 'dp'`

## Cause

pyOCD 0.35.0 changed the DPConnector constructor signature, breaking callers that passed only the probe.

## Fix

The maintainer planned to revert the API change; alternatively pass the debug port explicitly as second argument.

## Source

Resolution: fixed-in-release

Versions: 0.35.0

From [pyocd/pyOCD #1549](https://github.com/pyocd/pyOCD/issues/1549), summarized in own words; confidence medium, not reviewed yet.
