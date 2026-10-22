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
summary: "The csolution run was given a type filter entry with a leading '.' (build-type) whose name matches no build type defined in the solution."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4076-4087", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4093-4096", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4050-4062"]
---

## Symptom

`build-type '.<…>' does not exist in solution<…>, did you mean '+<…>'?<…>`

## Cause

The csolution run was given a type filter entry with a leading '.' (build-type) whose name matches no build type defined in the solution. The name is collected from the solution's build-types and from their context maps, and CheckTypeFilterSpelling records it as missing from that set. The <…> in the message is the filter's name without the '.' prefix. If the same name exists as a target type, the message adds the hint that the user probably meant the '+' prefix, which selects target types.

## Fix

Find the filter entry that uses the named type with a '.' prefix and correct it. Use '.<name>' only when <name> is a build type defined in the solution's build-types section. If <name> is a target type, write it as '+<name>' instead, as the hint says. The warning is printed once per missing name in the include and exclude filters.

## Note

The message has no code and the README does not document it. The '.' and '+' hint is a string check on the name, so a name that exists as both a build type and a target type is never flagged as misspelled. The warning text is built in PrintMissingFilters, which is outside the lines given, but it is read in full from 4095-4096.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4076-4087`
- `tools/projmgr/src/ProjMgrWorker.cpp:4093-4096`
- `tools/projmgr/src/ProjMgrWorker.cpp:4050-4062`
