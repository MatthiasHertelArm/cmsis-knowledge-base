---
id: "iss-cpackget-122"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget init fails with 'no such host' behind a proxy after a toolbox update"
summary: "cpackget 0.8.0 (toolbox 1.1.0) has a bug in its proxy handling, while 0.7.0 worked through the same proxy."
status: "draft"
tool: "cpackget"
symptoms: ["E: Get \"https://www.keil.com/pack/keil.pidx\": dial tcp: lookup www.keil.com: no such host", "E: failed to download file"]
symptom_regex: "E:\\s+Get\\s+\".*?\":\\s+dial\\s+tcp:\\s+lookup\\s+www\\.keil\\.com:\\s+no\\s+such\\s+host"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/122"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/122"
resolution: "unresolved"
versions: "cpackget 0.8.0 (toolbox 1.1.0) affected; 0.7.0 (toolbox 1.0.0) works"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "https://www.keil.com/pack/keil.pidx": dial tcp: lookup www.keil.com: no such host`
`E: failed to download file`

## Cause

cpackget 0.8.0 (toolbox 1.1.0) has a bug in its proxy handling, while 0.7.0 worked through the same proxy. For https URLs only HTTPS_PROXY applies, and it needs a proxy with a valid certificate; HTTP_PROXY has no effect.

## Fix

Set HTTPS_PROXY to the proxy (with a valid certificate). For the 0.8.0 proxy bug the maintainer offered a test build v0.8.1-alpha.1 from a personal fork, not confirmed in the thread; cpackget 0.7.0 from toolbox 1.0.0 still worked for the reporter.

## Source

Resolution: unresolved

Versions: cpackget 0.8.0 (toolbox 1.1.0) affected; 0.7.0 (toolbox 1.0.0) works

From [Open-CMSIS-Pack/cpackget #122](https://github.com/Open-CMSIS-Pack/cpackget/issues/122), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
