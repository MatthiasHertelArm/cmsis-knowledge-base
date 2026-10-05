---
id: "iss-pyocd-923"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack -u fails to download the index or pack descriptors from keil.com"
summary: "The index and pack descriptor downloads failed because of a server-side problem at the pack host, not a pyOCD bug; some pdsc URLs returned HTML pages."
status: "draft"
tool: "pyocd"
symptoms: ["ERRO https://www.keil.com/pack/index.pidx: error trying to connect: unexpected end of file", "ERRO download of \"http://www.keil.com/pack/ARM.minar.pdsc\" failed: unexpected end of file"]
symptom_regex: "https:/\\S+:\\s+error\\s+trying\\s+to\\s+connect:\\s+unexpected\\s+end\\s+of\\s+file"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/923"
doc_source: "https://github.com/pyocd/pyOCD/issues/923"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERRO https://www.keil.com/pack/index.pidx: error trying to connect: unexpected end of file`
`ERRO download of "http://www.keil.com/pack/ARM.minar.pdsc" failed: unexpected end of file`

## Cause

The index and pack descriptor downloads failed because of a server-side problem at the pack host, not a pyOCD bug; some pdsc URLs returned HTML pages.

## Fix

Retry: the maintainers worked around it on the server and reported it fixed (a retest during the server change could still fail). Failures for a few vendors (e.g. Qorvo) are known and outside pyOCD's control.

## Source

Resolution: not-a-bug

From [pyocd/pyOCD #923](https://github.com/pyocd/pyOCD/issues/923), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
