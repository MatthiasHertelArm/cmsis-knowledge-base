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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4099"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A type filter selects a target-type '+X' that the solution does not define, so the name is not in the solution's target-type list."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4076-4088", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4098-4101"]
---

## Symptom

`target-type '+<…>' does not exist in solution<…>, did you mean '.<…>'?<…>`

## Cause

A type filter selects a target-type '+X' that the solution does not define, so the name is not in the solution's target-type list. CheckTypeFilterSpelling sets the 'misspelled' flag when that same name is a build-type, so the user has written the wrong prefix for a name that exists as a build-type. Only the name in the message is known from the source; the filter's origin (context selector or command-line filter) is not shown in the given lines.

## Fix

Replace the '+X' filter with '.X' wherever the filter is written, so the name is matched as a build-type. Then rerun the build. If X is meant as a target-type, define it in the solution's target-types or correct its spelling so it matches a defined target-type.

## Note

The warning appears only when the name is misspelled as a target-type and the same name is a known build-type; otherwise the suggestion part is omitted. The message ends with '<…>' in the template, which is the solution name or a trailing context part, not a separate clause. The message code is empty in the catalog entry.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4076-4088`
- `tools/projmgr/src/ProjMgrWorker.cpp:4098-4101`
