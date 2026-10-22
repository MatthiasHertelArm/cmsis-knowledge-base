---
id: "iss-toolbox-716"
type: "troubleshooting"
domain: "project"
title: "csolution: Run Configuration Generator fails when several projects of a solution share a generator"
summary: "Launching Run Configuration Generator for a solution with two or more projects that use the same single-project generator fails with the 'one or more selected contexts are unrelated' error."
status: "draft"
tool: "csolution"
symptoms: ["one or more selected contexts are unrelated, redefine the '--context arg [...]' option"]
symptom_regex: "one\\s+or\\s+more\\s+selected\\s+contexts\\s+are\\s+unrelated,\\s+redefine\\s+the\\s+'.*?'\\s+option"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/716"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/716"
resolution: "workaround"
versions: "nightly build 2026-10-09"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`one or more selected contexts are unrelated, redefine the '--context arg [...]' option`

## Cause

Launching Run Configuration Generator for a solution with two or more projects that use the same single-project generator fails with the 'one or more selected contexts are unrelated' error.

## Fix

Work around it by selecting one project for the active context, running its generator, and repeating for each remaining project. Once all projects are configured, multiple projects can be selected again for build and debug. Comment 1 reports that generators can be launched for each individual project in nightly build 2026-10-09.

## Source

Resolution: workaround

Versions: nightly build 2026-10-09

From [Open-CMSIS-Pack/cmsis-toolbox #716](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/716), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
