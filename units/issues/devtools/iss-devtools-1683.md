---
id: "iss-devtools-1683"
type: "troubleshooting"
domain: "project"
title: "csolution: Error that source modules are added by multiple components since 2.5.0"
summary: "Since CMSIS-Toolbox 2.5.0 the default CMake generator (cbuild2cmake) builds per component, so the same source file listed by two components would give multiple objects with the same symbols at link time."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: source modules added by multiple components:"]
symptom_regex: "source\\s+modules\\s+added\\s+by\\s+multiple\\s+components:"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1683"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1683"
resolution: "workaround"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: source modules added by multiple components:`

## Cause

Since CMSIS-Toolbox 2.5.0 the default CMake generator (cbuild2cmake) builds per component, so the same source file listed by two components would give multiple objects with the same symbols at link time. The check is intended; in cbuildgen mode it is only a warning.

## Fix

Fix the pack so the file belongs to one component. Short term: run cbuild with --cbuildgen, or pin the toolbox to 2.4.0 in vcpkg-configuration.json (the CMSIS Solution Build button cannot pass --cbuildgen). The maintainers announced that duplicated files would be hidden from subsequent components.

## Source

Resolution: workaround

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1683](https://github.com/Open-CMSIS-Pack/devtools/issues/1683), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
