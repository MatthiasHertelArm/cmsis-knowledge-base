---
id: "iss-pyocd-1766"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: nRF9160/nRF91x1 shows APPROTECT enabled and 'No cores were discovered' with older pyOCD"
summary: "pyOCD reports APPROTECT enabled on nRF91 devices (nRF9151/nRF9161 used with the nrf9160_xxaa target) although the user never enabled it, and unlocks by mass erase, which also wipes the settings storage."
status: "draft"
tool: "pyocd"
symptoms: ["W nRF9160_xxAA APPROTECT enabled: will try to unlock via mass erase [target_nRF91]", "C No cores were discovered! [__main__]"]
symptom_regex: "W\\s+nRF9160_xxAA\\s+APPROTECT\\s+enabled:\\s+will\\s+try\\s+to\\s+unlock\\s+via\\s+mass\\s+erase"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1766"
doc_source: "https://github.com/pyocd/pyOCD/issues/1766"
resolution: "workaround"
versions: "Reported on 0.36.0; 'No cores were discovered' on 0.35.1; loading works on 0.38.0 and 0.39.0"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["nRF91 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W nRF9160_xxAA APPROTECT enabled: will try to unlock via mass erase [target_nRF91]`
`C No cores were discovered! [__main__]`

## Cause

pyOCD reports APPROTECT enabled on nRF91 devices (nRF9151/nRF9161 used with the nrf9160_xxaa target) although the user never enabled it, and unlocks by mass erase, which also wipes the settings storage. The thread gives no root cause. With pyOCD 0.35.1 the mass erase was followed by 'No cores were discovered'.

## Fix

To get loading working again, upgrade pyOCD (one user went from 0.35.1 to 0.39.0; the APPROTECT warning and mass erase still appear, but the load succeeds). An explicit chip erase (pyocd load -e chip, or pyocd erase -c) was also suggested. With the newer version, run the modem firmware update with -t nrf91.

## Source

Resolution: workaround

Versions: Reported on 0.36.0; 'No cores were discovered' on 0.35.1; loading works on 0.38.0 and 0.39.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1766](https://github.com/pyocd/pyOCD/issues/1766), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
