---
id: "iss-toolbox-716"
type: "troubleshooting"
domain: "project"
title: "csolution: Run Configuration Generator fails when several projects of a solution share one generator"
summary: "When a solution has several projects that use the same single-project generator, the generator run is given the selected contexts of those projects together, and the tool reports them as unrelated and stops."
status: "draft"
tool: "csolution"
symptoms: ["one or more selected contexts are unrelated, redefine the '--context arg [...]' option"]
symptom_regex: "one\\s+or\\s+more\\s+selected\\s+contexts\\s+are\\s+unrelated,\\s+redefine\\s+the\\s+'.*?'\\s+option"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/716"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/716"
resolution: "workaround"
versions: "Validated in nightly build 2026-10-09; no release number named in the thread"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`one or more selected contexts are unrelated, redefine the '--context arg [...]' option`

## Cause

When a solution has several projects that use the same single-project generator, the generator run is given the selected contexts of those projects together, and the tool reports them as unrelated and stops.

## Fix

Workaround: select only one project as the active context, run the generator for it, and repeat for each other project; afterwards multiple projects can be selected again for build and debug.

## Source

Resolution: workaround

Versions: Validated in nightly build 2026-10-09; no release number named in the thread

From [Open-CMSIS-Pack/cmsis-toolbox #716](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/716), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
