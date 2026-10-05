---
id: "iss-cpackget-90"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget init fails with 'expected element type <index> but have <html>'"
summary: "The index URL was given without www; keil.com redirects to a web page, so an HTML document was downloaded instead of index.pidx."
status: "draft"
tool: "cpackget"
symptoms: ["E: expected element type <index> but have <html>"]
symptom_regex: "E:\\s+expected\\s+element\\s+type\\s+<index>\\s+but\\s+have\\s+<html>"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/90"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/90"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: expected element type <index> but have <html>`

## Cause

The index URL was given without www; keil.com redirects to a web page, so an HTML document was downloaded instead of index.pidx.

## Fix

Use the exact URL https://www.keil.com/pack/index.pidx.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/cpackget #90](https://github.com/Open-CMSIS-Pack/cpackget/issues/90), summarized in own words; confidence high, checked against the thread, not reviewed yet.
