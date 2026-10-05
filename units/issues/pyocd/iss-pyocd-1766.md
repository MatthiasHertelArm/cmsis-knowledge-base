---
id: "iss-pyocd-1766"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: nRF9160/nRF91x1 shows APPROTECT enabled and 'No cores were discovered' with older pyOCD"
summary: "Older pyOCD releases misdetect or mishandle APPROTECT on nRF91 devices and trigger a mass erase, which also wipes settings storage; with some versions no core is found afterwards."
status: "draft"
tool: "pyocd"
symptoms: ["W nRF9160_xxAA APPROTECT enabled: will try to unlock via mass erase [target_nRF91]", "C No cores were discovered! [__main__]"]
symptom_regex: "W\\s+nRF9160_xxAA\\s+APPROTECT\\s+enabled:\\s+will\\s+try\\s+to\\s+unlock\\s+via\\s+mass\\s+erase"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1766"
doc_source: "https://github.com/pyocd/pyOCD/issues/1766"
resolution: "workaround"
versions: "Reported with 0.35.1, fixed by upgrading to 0.39.0."
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["nRF91 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W nRF9160_xxAA APPROTECT enabled: will try to unlock via mass erase [target_nRF91]`
`C No cores were discovered! [__main__]`

## Cause

Older pyOCD releases misdetect or mishandle APPROTECT on nRF91 devices and trigger a mass erase, which also wipes settings storage; with some versions no core is found afterwards. One user found the older release was the problem.

## Fix

Upgrade pyOCD (0.35.1 to 0.39.0 fixed it for one user). An explicit chip erase (pyocd load -e chip, or pyocd erase -c) was also suggested. With newer versions, use -t nrf91 for the modem firmware update command.

## Source

Resolution: workaround

Versions: Reported with 0.35.1, fixed by upgrading to 0.39.0.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1766](https://github.com/pyocd/pyOCD/issues/1766), summarized in own words; confidence low, not reviewed yet.
