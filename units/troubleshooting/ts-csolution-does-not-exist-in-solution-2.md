---
id: "ts-csolution-does-not-exist-in-solution-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: target-type '+…' does not exist in solution…, did you mean '.…'?…"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["target-type '+<…>' does not exist in solution<…>, did you mean '.<…>'?<…>"]
symptom_regex: "^target\\-type '\\+.+?' does not exist in solution.+?, did you mean '\\..+?'\\?.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:4099"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `for-context:` or `not-for-context:` entry refers to target type `+<name>`, but the csolution.yml has no target type of that name, so the filter never matches."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4076", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4099", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/typefilters.cproject.yml:17", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5508"]
---

## Symptom

`target-type '+<…>' does not exist in solution<…>, did you mean '.<…>'?<…>`

## Cause

A `for-context:` or `not-for-context:` entry refers to target type `+<name>`, but the csolution.yml has no target type of that name, so the filter never matches. If a build type of that name exists, csolution suggests `.<name>`: `.` and `+` were mixed up.

## Fix

Use an existing target type after `+`, or write `.<name>` when a build type is meant, e.g. `for-context: .Debug` instead of `for-context: +Debug`.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4076`
- `tools/projmgr/src/ProjMgrWorker.cpp:4099`
- `tools/projmgr/test/data/TestSolution/typefilters.cproject.yml:17`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5508`
