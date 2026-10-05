---
id: "iss-cpackget-166"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of a keil.com URL fails with an expired certificate error"
summary: "The URL without www points to a host with an expired certificate; the official pack host is www.keil.com."
status: "draft"
tool: "cpackget"
symptoms: ["E: Get \"https://keil.com/pack/ARM.CMSIS.5.9.0.pack\": tls: failed to verify certificate: x509: certificate has expired or is not yet valid"]
symptom_regex: "E:\\s+Get\\s+\".*?\":\\s+tls:\\s+failed\\s+to\\s+verify\\s+certificate:\\s+x509:\\s+certificate\\s+has\\s+expired\\s+or\\s+is\\s+not\\s+yet\\s+valid"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/166"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/166"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "https://keil.com/pack/ARM.CMSIS.5.9.0.pack": tls: failed to verify certificate: x509: certificate has expired or is not yet valid`

## Cause

The URL without www points to a host with an expired certificate; the official pack host is www.keil.com. Typing URLs by hand also bypasses the index lookup.

## Fix

Use cpackget add ARM::CMSIS@5.9.0 so cpackget resolves the URL from the index, or use https://www.keil.com/pack/... in the URL.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/cpackget #166](https://github.com/Open-CMSIS-Pack/cpackget/issues/166), summarized in own words; confidence high, checked against the thread, not reviewed yet.
