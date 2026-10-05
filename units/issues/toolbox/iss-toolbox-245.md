---
id: "iss-toolbox-245"
type: "troubleshooting"
domain: "project"
title: "cbuild: 2.7.0 rejects linker regions header that an executes step generates"
summary: "csolution 2.7.0 checks the regions header before the build, so a file produced by an executes node does not exist yet."
status: "draft"
tool: "cbuild"
symptoms: ["error csolution: specified regions header was not found"]
symptom_regex: "specified\\s+regions\\s+header\\s+was\\s+not\\s+found"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/245"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/245"
resolution: "fixed-in-release"
versions: "2.7.0; fixed in 2.8.0 era"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: specified regions header was not found`

## Cause

csolution 2.7.0 checks the regions header before the build, so a file produced by an executes node does not exist yet.

## Fix

Create the file beforehand (touch) as workaround. Fixed by treating it like user files in devtools PR 1921, in the next release.

## Source

Resolution: fixed-in-release

Versions: 2.7.0; fixed in 2.8.0 era

From [Open-CMSIS-Pack/cmsis-toolbox #245](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/245), summarized in own words; confidence high, not reviewed yet.
