---
id: "iss-devtools-528"
type: "troubleshooting"
domain: "project"
title: "csolution: Old yml projects fail the schema check: optimize and warnings values changed in 1.2"
summary: "Schema 1.2 replaced the optimize values (max, size, speed, debug) by size, speed, balanced, none and the warnings values (no, all, Misra, AC5-like) by on and off; the old values had never been processed by the tools."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/528"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/528"
resolution: "not-a-bug"
versions: "schema 1.1 to 1.2"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Schema 1.2 replaced the optimize values (max, size, speed, debug) by size, speed, balanced, none and the warnings values (no, all, Misra, AC5-like) by on and off; the old values had never been processed by the tools.

## Fix

Edit the yml files to the new values. It is a deliberate compatibility break of the schema.

## Source

Resolution: not-a-bug

Versions: schema 1.1 to 1.2

From [Open-CMSIS-Pack/devtools #528](https://github.com/Open-CMSIS-Pack/devtools/issues/528), summarized in own words; confidence high, checked against the thread, not reviewed yet.
