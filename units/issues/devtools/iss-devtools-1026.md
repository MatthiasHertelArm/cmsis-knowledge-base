---
id: "iss-devtools-1026"
type: "troubleshooting"
domain: "project"
title: "csolution: Context set with several -c values or a comma list behaves unexpectedly"
summary: "Several contexts can be given as repeated -c options or as one comma-separated list, but there must be no space after a comma, otherwise the second name is not read as part of the option."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1026"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1026"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Several contexts can be given as repeated -c options or as one comma-separated list, but there must be no space after a comma, otherwise the second name is not read as part of the option.

## Fix

Use csolution convert <solution> -c cm33_s.Debug+AVH -c cm33_ns.Release+AVH, or -c a,b without spaces.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #1026](https://github.com/Open-CMSIS-Pack/devtools/issues/1026), summarized in own words; confidence high, checked against the thread, not reviewed yet.
