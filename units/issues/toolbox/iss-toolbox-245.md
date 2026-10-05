---
id: "iss-toolbox-245"
type: "troubleshooting"
domain: "project"
title: "cbuild: 2.7.0 rejects linker regions header that an executes step generates"
summary: "csolution 2.7.0 checks the regions header before the build, so a file produced by an executes node does not exist yet (2.6.1 only warned)."
status: "draft"
tool: "cbuild"
symptoms: ["error csolution: specified regions header was not found"]
symptom_regex: "specified\\s+regions\\s+header\\s+was\\s+not\\s+found"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/245"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/245"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.7.0 affected; 2.6.1 only warned"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: specified regions header was not found`

## Cause

csolution 2.7.0 checks the regions header before the build, so a file produced by an executes node does not exist yet (2.6.1 only warned).

## Fix

Create the file beforehand (touch) as a workaround. Devtools PR 1921 treats it like user files; it was merged for the next nightly build and the reporter confirmed the fix; no release is named.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.7.0 affected; 2.6.1 only warned

From [Open-CMSIS-Pack/cmsis-toolbox #245](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/245), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
