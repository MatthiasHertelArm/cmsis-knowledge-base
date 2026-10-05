---
id: "iss-devtools-815"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv: DerivedFrom not found when enumeratedValues has the same name as its field"
summary: "svdconv's derive lookup first checks whether the referenced name equals the current item (a shortcut for named and unnamed containers), and when the types differ (field vs enumeratedValues) it reports derivedFrom as not found."
status: "draft"
tool: "svdconv"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/815"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/815"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

svdconv's derive lookup first checks whether the referenced name equals the current item (a shortcut for named and unnamed containers), and when the types differ (field vs enumeratedValues) it reports derivedFrom as not found.

## Fix

Give the enumeratedValues container a name different from its field name and refer to it by full path from the peripheral level if needed. A real fix of the derive mechanism was postponed.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #815](https://github.com/Open-CMSIS-Pack/devtools/issues/815), summarized in own words; confidence medium, not reviewed yet.
