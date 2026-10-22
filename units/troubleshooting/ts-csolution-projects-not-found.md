---
id: "ts-csolution-projects-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: projects not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["projects not found"]
symptom_regex: "^projects not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:505"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution.yml lists no project: `projects:` is missing or empty and there is no `west:` or `cmake:` entry."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:505", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1286", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/missing_projects.csolution.yml:3", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5198"]
---

## Symptom

`projects not found`

## Cause

The csolution.yml lists no project: `projects:` is missing or empty and there is no `west:` or `cmake:` entry. Only a solution whose target sets contain `images:` without any `project-context:` (an image-only solution) may do without projects.

## Fix

Add the projects under `projects:` in the csolution.yml, e.g. `projects:` followed by `  - project: ./blinky/blinky.cproject.yml`.

## Trigger in the source

```cpp
if (!IsSolutionImageOnly() && cprojects.empty() && m_parser.GetCsolution().westApps.empty() && m_parser.GetCsolution().cmakeApps.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:505`
- `tools/projmgr/src/ProjMgr.cpp:1286`
- `tools/projmgr/test/data/TestSolution/missing_projects.csolution.yml:3`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5198`
