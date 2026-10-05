---
id: "iss-cpackget-122"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget init fails with 'no such host' behind a proxy after a toolbox update"
summary: "A proxy handling bug in the HTTP client of cpackget 0.8.0; HTTPS downloads through a proxy also need HTTPS_PROXY pointing to a proxy with a trusted certificate (HTTP_PROXY alone does not apply to https URLs)."
status: "draft"
tool: "cpackget"
symptoms: ["E: Get \"https://www.keil.com/pack/keil.pidx\": dial tcp: lookup www.keil.com: no such host", "E: failed to download file"]
symptom_regex: "E:\\s+Get\\s+\".*?\":\\s+dial\\s+tcp:\\s+lookup\\s+www\\.keil\\.com:\\s+no\\s+such\\s+host"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/122"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/122"
resolution: "fixed-in-release"
versions: "0.8.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "https://www.keil.com/pack/keil.pidx": dial tcp: lookup www.keil.com: no such host`
`E: failed to download file`

## Cause

A proxy handling bug in the HTTP client of cpackget 0.8.0; HTTPS downloads through a proxy also need HTTPS_PROXY pointing to a proxy with a trusted certificate (HTTP_PROXY alone does not apply to https URLs).

## Fix

Update cpackget beyond 0.8.0 and set HTTPS_PROXY (and HTTP_PROXY) to the corporate proxy.

## Source

Resolution: fixed-in-release

Versions: 0.8.0

From [Open-CMSIS-Pack/cpackget #122](https://github.com/Open-CMSIS-Pack/cpackget/issues/122), summarized in own words; confidence medium, not reviewed yet.
