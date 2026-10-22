---
id: "ts-csolution-does-not-exist-in-solution"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: build-type '.…' does not exist in solution…, did you mean '+…'?…"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["build-type '.<…>' does not exist in solution<…>, did you mean '+<…>'?<…>"]
symptom_regex: "^build\\-type '\\..+?' does not exist in solution.+?, did you mean '\\+.+?'\\?.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4095"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `for-context:` or `not-for-context:` entry in a csolution.yml, cproject.yml or clayer.yml uses `.Name`, but Name is not a build type defined under build-types: (nor in a context-map:)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4012-4105", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5508-5531", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/typefilters.cproject.yml", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/typefilters.csolution.yml"]
---

## Symptom

`build-type '.<…>' does not exist in solution<…>, did you mean '+<…>'?<…>`

## Cause

A `for-context:` or `not-for-context:` entry in a csolution.yml, cproject.yml or clayer.yml uses `.Name`, but Name is not a build type defined under build-types: (nor in a context-map:). When Name is a target type, the warning asks whether `+Name` was meant, since `.` marks build types and `+` target types. The same check prints `target-type '+Name' does not exist in solution` for unknown target types.

## Fix

Correct the filter, e.g. `for-context: .Debug` for a build type or `for-context: +CM3` for a target type, or add the missing type under build-types:/target-types: in the csolution.yml. Names are case-sensitive.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4012-4105`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5508-5531`
- `tools/projmgr/test/data/TestSolution/typefilters.cproject.yml`
- `tools/projmgr/test/data/TestSolution/typefilters.csolution.yml`
