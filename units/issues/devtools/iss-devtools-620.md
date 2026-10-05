---
id: "iss-devtools-620"
type: "troubleshooting"
domain: "project"
title: "cbuild: Files declared as headerC/includeC in a pack are missing from the include search path"
summary: "The tools only implemented the pack specification up to 1.7.7, so the language-specific file categories headerC and includeC were ignored; only header/include added -I paths."
status: "draft"
tool: "cbuild"
symptoms: ["fatal error: 'c_specific_header.h' file not found"]
symptom_regex: "fatal\\s+error:\\s+'.*?'\\s+file\\s+not\\s+found"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/620"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/620"
resolution: "fixed-in-release"
versions: "cbuild 1.3.0; language/scope attributes in 2.5.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`fatal error: 'c_specific_header.h' file not found`

## Cause

The tools only implemented the pack specification up to 1.7.7, so the language-specific file categories headerC and includeC were ignored; only header/include added -I paths.

## Fix

Use the plain header/include categories, or move to CMSIS-Toolbox 2.5.0 or later where cbuild2cmake supports the language and scope attributes.

## Source

Resolution: fixed-in-release

Versions: cbuild 1.3.0; language/scope attributes in 2.5.0

From [Open-CMSIS-Pack/devtools #620](https://github.com/Open-CMSIS-Pack/devtools/issues/620), summarized in own words; confidence high, checked against the thread, not reviewed yet.
