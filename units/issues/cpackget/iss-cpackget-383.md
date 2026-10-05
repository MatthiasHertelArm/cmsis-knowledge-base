---
id: "iss-cpackget-383"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add Vendor::Pack@>=3.0.0 silently does nothing on the Windows command line"
summary: "The shell treats > as output redirection before cpackget starts, so the version text becomes a file name and the message goes into that file."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/383"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/383"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The shell treats > as output redirection before cpackget starts, so the version text becomes a file name and the message goes into that file. The same applies to ^ in cmd.

## Fix

Quote the pack specification: cpackget add "Keil::STM32U5xx_DFP@>=3.0.0" or "Vendor::Pack@^3.0.0".

## Source

Resolution: user-error

From [Open-CMSIS-Pack/cpackget #383](https://github.com/Open-CMSIS-Pack/cpackget/issues/383), summarized in own words; confidence high, checked against the thread, not reviewed yet.
