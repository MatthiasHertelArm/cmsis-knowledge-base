---
id: "iss-devtools-1052"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk does not warn about missing Cvariant components referenced in accept"
summary: "The RTE model only reports a missing component (M504) for require expressions; components named only in accept conditions were not checked, so a missing variant went unnoticed."
status: "draft"
tool: "packchk"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1052"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1052"
resolution: "fixed-in-release"
versions: "before 1.4"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The RTE model only reports a missing component (M504) for require expressions; components named only in accept conditions were not checked, so a missing variant went unnoticed.

## Fix

packchk was extended to check all references; as a quick test temporarily change accept to require to see M504 messages for missing components.

## Source

Resolution: fixed-in-release

Versions: before 1.4

From [Open-CMSIS-Pack/devtools #1052](https://github.com/Open-CMSIS-Pack/devtools/issues/1052), summarized in own words; confidence medium, not reviewed yet.
