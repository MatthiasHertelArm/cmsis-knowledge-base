---
id: "iss-cpackget-68"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add behind a VPN/proxy fails and later errors with 'zip: not a valid zip file'"
summary: "The proxy was not configured the way cpackget expects; with the http_proxy environment variable set (see cpackget's 'working behind a proxy' notes) the download works."
status: "draft"
tool: "cpackget"
symptoms: ["E: Get \"http://www.keil.com/pack/Keil.STM32F1xx_DFP.2.4.0.pack\": dial tcp 23.11.231.137:80: connectex: No connection could be made because the target machine actively refused it.", "E: Can't decompress \"<packs>\\.Download\\Keil.STM32F1xx_DFP.2.4.0.pack\": zip: not a valid zip file"]
symptom_regex: "E:\\s+Get\\s+\".*?\":\\s+dial\\s+tcp\\s+\\S+:\\S+:\\s+connectex:\\s+No\\s+connection\\s+could\\s+be\\s+made\\s+because\\s+the\\s+target\\s+machine\\s+actively\\s+refused\\s+it\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/68"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/68"
resolution: "workaround"
versions: "0.4.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "http://www.keil.com/pack/Keil.STM32F1xx_DFP.2.4.0.pack": dial tcp 23.11.231.137:80: connectex: No connection could be made because the target machine actively refused it.`
`E: Can't decompress "<packs>\.Download\Keil.STM32F1xx_DFP.2.4.0.pack": zip: not a valid zip file`

## Cause

The proxy was not configured the way cpackget expects; with the http_proxy environment variable set (see cpackget's 'working behind a proxy' notes) the download works. The failed download left a 0-byte pack in .Download that was reused on the next run instead of downloaded again, because cpackget only removed the file when unzipping failed.

## Fix

Set http_proxy for the shell and delete the empty pack file from .Download. PR #69 removes the file after HTTP errors too, expected in the next release.

## Source

Resolution: workaround

Versions: 0.4.0

From [Open-CMSIS-Pack/cpackget #68](https://github.com/Open-CMSIS-Pack/cpackget/issues/68), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
