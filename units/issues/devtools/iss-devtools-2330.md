---
id: "iss-devtools-2330"
type: "troubleshooting"
domain: "project"
title: "csolution: Schema check rejects define values with C integer suffixes U, UL, ULL"
summary: "The JSON schema pattern for define: values did not allow C-style suffixes on hex or decimal numbers."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2330"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2330"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The JSON schema pattern for define: values did not allow C-style suffixes on hex or decimal numbers.

## Fix

Schema extended; the allowed forms are now described in the define: section of the YML input format documentation. Update the toolbox if the schema check still rejects such a value.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #2330](https://github.com/Open-CMSIS-Pack/devtools/issues/2330), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
