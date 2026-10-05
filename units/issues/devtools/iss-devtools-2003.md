---
id: "iss-devtools-2003"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml invalid: empty debug sequence block gives unexpected instance type"
summary: "An empty <block/> in a pack's debug sequence (or one containing only comments) was written as an empty map into cbuild-run.yml, which then failed its own schema check."
status: "draft"
tool: "csolution"
symptoms: ["/Simple+MCXN947VDF.cbuild-run.yml:193:11 - error csolution: unexpected instance type"]
symptom_regex: "unexpected\\s+instance\\s+type"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2003"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2003"
resolution: "fixed-in-release"
versions: "2.8.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"], "device": ["MCXN947"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`/Simple+MCXN947VDF.cbuild-run.yml:193:11 - error csolution: unexpected instance type`

## Cause

An empty <block/> in a pack's debug sequence (or one containing only comments) was written as an empty map into cbuild-run.yml, which then failed its own schema check.

## Fix

Fixed in toolbox nightly 435 and later: empty blocks are no longer emitted. Workaround before: remove the empty <block/> from the pdsc.

## Source

Resolution: fixed-in-release

Versions: 2.8.0

From [Open-CMSIS-Pack/devtools #2003](https://github.com/Open-CMSIS-Pack/devtools/issues/2003), summarized in own words; confidence high, checked against the thread, not reviewed yet.
