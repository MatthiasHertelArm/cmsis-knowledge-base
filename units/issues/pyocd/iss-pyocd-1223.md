---
id: "iss-pyocd-1223"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack update reports certificate errors and 404s for some vendors"
summary: "Some vendor servers have expired TLS certificates or incomplete chains that browsers tolerate but cmsis-pack-manager does not; 404s were a known cmsis-pack-manager defect."
status: "draft"
tool: "pyocd"
symptoms: ["error trying to connect: invalid certificate: CertExpired", "error trying to connect: invalid certificate: UnknownIssuer"]
symptom_regex: "error\\s+trying\\s+to\\s+connect:\\s+invalid\\s+certificate:\\s+CertExpired"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1223"
doc_source: "https://github.com/pyocd/pyOCD/issues/1223"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error trying to connect: invalid certificate: CertExpired`
`error trying to connect: invalid certificate: UnknownIssuer`

## Cause

Some vendor servers have expired TLS certificates or incomplete chains that browsers tolerate but cmsis-pack-manager does not; 404s were a known cmsis-pack-manager defect.

## Fix

Only vendors' own sites must fix this. Download the packs manually from the Keil pack list and use pyocd --pack <file>.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1223](https://github.com/pyocd/pyOCD/issues/1223), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
