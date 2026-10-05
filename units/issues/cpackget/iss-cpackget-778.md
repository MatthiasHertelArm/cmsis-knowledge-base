---
id: "iss-cpackget-778"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget init: 'remote server is offline or cannot be reached' though browser works"
summary: "cpackget checks connectivity by downloading a small index file first."
status: "draft"
tool: "cpackget"
symptoms: ["E: \"https://www.keil.com/pack/keil.vidx\": remote server is offline or cannot be reached"]
symptom_regex: "E:\\s+\".*?\":\\s+remote\\s+server\\s+is\\s+offline\\s+or\\s+cannot\\s+be\\s+reached"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/778"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/778"
resolution: "configuration"
versions: "cpackget 2.2.1 / CMSIS-Toolbox 2.14.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: "https://www.keil.com/pack/keil.vidx": remote server is offline or cannot be reached`

## Cause

cpackget checks connectivity by downloading a small index file first. In the reported case the machine had an empty /etc/resolv.conf (systemd-resolved setup), so Go could not resolve host names even though curl with redirects seemed to work elsewhere. Proxy and CA-store problems produce the same message.

## Fix

Check name resolution (on systemd-resolved link /etc/resolv.conf to the resolved stub file), then check HTTP_PROXY/HTTPS_PROXY/NO_PROXY and the system CA bundle, and test the keil.com pack URLs with curl -L. Not a cpackget defect.

## Source

Resolution: configuration

Versions: cpackget 2.2.1 / CMSIS-Toolbox 2.14.1

From [Open-CMSIS-Pack/cpackget #778](https://github.com/Open-CMSIS-Pack/cpackget/issues/778), summarized in own words; confidence medium, not reviewed yet.
