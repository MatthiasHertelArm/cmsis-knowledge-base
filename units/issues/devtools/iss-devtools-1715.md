---
id: "iss-devtools-1715"
type: "troubleshooting"
domain: "project"
title: "csolution: cmse-lib access sequence error for the non-secure project since 2.5.0"
summary: "From 2.5.0 the CMake backend resolves $cmse-lib(project)$ to the selected build of the secure project, so that project must be part of the same context set."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: context 'secure' referenced by access sequence 'cmse-lib' does not exist or is not selected", "*** ERROR M204:\n  Path not found: 'C:/xxx/non_secure/$cmse-lib(secure)!"]
symptom_regex: "context\\s+'.*?'\\s+referenced\\s+by\\s+access\\s+sequence\\s+'.*?'\\s+does\\s+not\\s+exist\\s+or\\s+is\\s+not\\s+selected"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1715"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1715"
resolution: "configuration"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: context 'secure' referenced by access sequence 'cmse-lib' does not exist or is not selected`
`*** ERROR M204:
  Path not found: 'C:/xxx/non_secure/$cmse-lib(secure)!`

## Cause

From 2.5.0 the CMake backend resolves $cmse-lib(project)$ to the selected build of the secure project, so that project must be part of the same context set. Building the non-secure context alone cannot resolve it (2.4.0 mapped it to the same build and target type by convention).

## Fix

Select both projects, for example cbuild <solution> --context CM33s.Release+CS300 --context CM33ns.Debug+CS300, or use a context-set for the whole target type.

## Source

Resolution: configuration

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1715](https://github.com/Open-CMSIS-Pack/devtools/issues/1715), summarized in own words; confidence high, not reviewed yet.
