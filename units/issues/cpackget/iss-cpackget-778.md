---
id: "iss-cpackget-778"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget init: 'remote server is offline or cannot be reached' though browser works"
summary: "Before downloading, cpackget checks the connection by fetching the Keil.vidx index; the error means that download failed."
status: "draft"
tool: "cpackget"
symptoms: ["E: \"https://www.keil.com/pack/keil.vidx\": remote server is offline or cannot be reached"]
symptom_regex: "E:\\s+\".*?\":\\s+remote\\s+server\\s+is\\s+offline\\s+or\\s+cannot\\s+be\\s+reached"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/778"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/778"
resolution: "configuration"
versions: "CMSIS-Toolbox 2.14.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: "https://www.keil.com/pack/keil.vidx": remote server is offline or cannot be reached`

## Cause

Before downloading, cpackget checks the connection by fetching the Keil.vidx index; the error means that download failed. In the reported case the DNS configuration was broken: /etc/resolv.conf was empty on a system using systemd-resolved, although curl requests to the pack URLs worked. Proxy settings and missing CA certificates were suggested as other possible causes.

## Fix

Fix the name resolution, for example on systemd-resolved link /run/systemd/resolve/resolv.conf to /etc/resolv.conf. Otherwise test the keil.com pack URLs with curl -L and check HTTP_PROXY/HTTPS_PROXY/NO_PROXY and the CA store, as the maintainers suggested. Not a cpackget defect.

## Source

Resolution: configuration

Versions: CMSIS-Toolbox 2.14.1

From [Open-CMSIS-Pack/cpackget #778](https://github.com/Open-CMSIS-Pack/cpackget/issues/778), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
