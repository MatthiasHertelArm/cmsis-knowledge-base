---
id: "iss-devtools-2510"
type: "troubleshooting"
domain: "project"
title: "csolution: Schema check rejects pname: under memory: in a target-type"
summary: "The documented memory: child node pname: was missing from the JSON schema, so the schema check failed although the documentation lists it."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2510"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2510"
resolution: "fixed-in-release"
versions: "seen in 2.14.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The documented memory: child node pname: was missing from the JSON schema, so the schema check failed although the documentation lists it.

## Fix

Fixed in a toolbox build after 2.14.1; update. Reporter confirmed with a nightly.

## Source

Resolution: fixed-in-release

Versions: seen in 2.14.1

From [Open-CMSIS-Pack/devtools #2510](https://github.com/Open-CMSIS-Pack/devtools/issues/2510), summarized in own words; confidence high, checked against the thread, not reviewed yet.
