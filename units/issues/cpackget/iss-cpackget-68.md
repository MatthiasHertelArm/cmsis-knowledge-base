---
id: "iss-cpackget-68"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add behind a VPN/proxy fails and later errors with 'zip: not a valid zip file'"
summary: "cpackget ignores Windows system proxy settings and only honours the http_proxy/https_proxy environment variables."
status: "draft"
tool: "cpackget"
symptoms: ["E: Get \"http://www.keil.com/pack/Keil.STM32F1xx_DFP.2.4.0.pack\": dial tcp 23.11.231.137:80: connectex: No connection could be made because the target machine actively refused it.", "E: Can't decompress \"<packs>\\.Download\\Keil.STM32F1xx_DFP.2.4.0.pack\": zip: not a valid zip file"]
symptom_regex: "E:\\s+Get\\s+\".*?\":\\s+dial\\s+tcp\\s+\\S+:\\S+:\\s+connectex:\\s+No\\s+connection\\s+could\\s+be\\s+made\\s+because\\s+the\\s+target\\s+machine\\s+actively\\s+refused\\s+it\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/68"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/68"
resolution: "workaround"
versions: "0.4.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "http://www.keil.com/pack/Keil.STM32F1xx_DFP.2.4.0.pack": dial tcp 23.11.231.137:80: connectex: No connection could be made because the target machine actively refused it.`
`E: Can't decompress "<packs>\.Download\Keil.STM32F1xx_DFP.2.4.0.pack": zip: not a valid zip file`

## Cause

cpackget ignores Windows system proxy settings and only honours the http_proxy/https_proxy environment variables. The failed download left a 0-byte file in .Download that was reused on the next run.

## Fix

Set http_proxy/https_proxy for the shell; delete the empty pack in .Download. Later releases remove failed downloads automatically.

## Source

Resolution: workaround

Versions: 0.4.0

From [Open-CMSIS-Pack/cpackget #68](https://github.com/Open-CMSIS-Pack/cpackget/issues/68), summarized in own words; confidence high, not reviewed yet.
