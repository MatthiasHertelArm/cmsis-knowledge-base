---
id: "iss-devtools-1683"
type: "troubleshooting"
domain: "project"
title: "csolution: Error that source modules are added by multiple components since 2.5.0"
summary: "Since CMSIS-Toolbox 2.5.0 the default CMake generator (cbuild2cmake) builds per component, so the same source file listed by two components would be compiled twice and clash at link time."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: source modules added by multiple components:"]
symptom_regex: "source\\s+modules\\s+added\\s+by\\s+multiple\\s+components:"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1683"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1683"
resolution: "workaround"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: source modules added by multiple components:`

## Cause

Since CMSIS-Toolbox 2.5.0 the default CMake generator (cbuild2cmake) builds per component, so the same source file listed by two components would be compiled twice and clash at link time. The check is intended; the older cbuildgen mode only warned.

## Fix

Fix the pack so the file belongs to one component. Short term: run cbuild with --cbuildgen, or pin the toolbox to 2.4.0 in vcpkg-configuration.json. Later toolbox versions hide the duplicate from the later component.

## Source

Resolution: workaround

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1683](https://github.com/Open-CMSIS-Pack/devtools/issues/1683), summarized in own words; confidence high, not reviewed yet.
