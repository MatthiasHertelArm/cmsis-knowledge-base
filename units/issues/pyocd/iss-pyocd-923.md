---
id: "iss-pyocd-923"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack -u fails to download the index or pack descriptors from keil.com"
summary: "The index download failed because of a server-side configuration problem at the pack host, not a pyOCD bug; some pdsc URLs returned HTML pages."
status: "draft"
tool: "pyocd"
symptoms: ["ERRO https://www.keil.com/pack/index.pidx: error trying to connect: unexpected end of file", "ERRO download of \"http://www.keil.com/pack/ARM.minar.pdsc\" failed: unexpected end of file"]
symptom_regex: "https:/\\S+:\\s+error\\s+trying\\s+to\\s+connect:\\s+unexpected\\s+end\\s+of\\s+file"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/923"
doc_source: "https://github.com/pyocd/pyOCD/issues/923"
resolution: "not-a-bug"
versions: "seen 2020"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERRO https://www.keil.com/pack/index.pidx: error trying to connect: unexpected end of file`
`ERRO download of "http://www.keil.com/pack/ARM.minar.pdsc" failed: unexpected end of file`

## Cause

The index download failed because of a server-side configuration problem at the pack host, not a pyOCD bug; some pdsc URLs returned HTML pages.

## Fix

Retry later: the maintainers fixed the server. If one pack still fails, download its .pack manually and use `--pack`.

## Source

Resolution: not-a-bug

Versions: seen 2020

From [pyocd/pyOCD #923](https://github.com/pyocd/pyOCD/issues/923), summarized in own words; confidence medium, not reviewed yet.
