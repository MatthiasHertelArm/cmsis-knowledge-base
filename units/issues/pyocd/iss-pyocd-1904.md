---
id: "iss-pyocd-1904"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pack install silently does nothing when index version differs from vendor pdsc"
summary: "The pack listed in the index has a newer version than what the vendor's pdsc or the download actually provides, so the expected version never appears locally and the part stays 'not installed'."
status: "draft"
tool: "pyocd"
symptoms: ["Downloading packs (press Control-C to cancel):"]
symptom_regex: "Downloading\\s+packs\\s+\\(press\\s+Control\\-C\\s+to\\s+cancel\\):"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1904"
doc_source: "https://github.com/pyocd/pyOCD/issues/1904"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Downloading packs (press Control-C to cancel):`

## Cause

The pack listed in the index has a newer version than what the vendor's pdsc or the download actually provides, so the expected version never appears locally and the part stays 'not installed'.

## Fix

Workaround reported: rename the locally cached pdsc to the version pyOCD expects (for example Holtek.HT32_DFP.1.0.75.pdsc to 1.0.76.pdsc). Retrying later worked for others once the versions matched.

## Source

Resolution: workaround

From [pyocd/pyOCD #1904](https://github.com/pyocd/pyOCD/issues/1904), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
