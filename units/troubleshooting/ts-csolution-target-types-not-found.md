---
id: "ts-csolution-target-types-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: target-types not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["target-types not found"]
symptom_regex: "^target\\-types not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:95"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProjMgrYamlParser::ParseCsolution calls ParseTargetTypes on the solution node of the .csolution.yml file and gets false back."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:94-97", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:86-87"]
---

## Symptom

`target-types not found`

## Cause

ProjMgrYamlParser::ParseCsolution calls ParseTargetTypes on the solution node of the .csolution.yml file and gets false back. The message is printed at line 95 with the input file path but no line number, so the failing entry is not located. The reason is inside ParseTargetTypes, whose body is not among the lines given. The message only says that parsing the target types of the solution failed.

## Fix

Open the .csolution.yml file named in the message and check the solution's target-types section: it must exist and each entry must be a well-formed target-type definition with a name. Correct the YAML and run the csolution command again. If the entry looks correct, check whether the tool prints a more specific error just before this one, since that message would name the failing item.

## Trigger in the source

```cpp
if (!ParseTargetTypes(solutionNode, csolution.path, csolution.targetTypes)) {
```

## Note

The failure reason is in ParseTargetTypes, which is not in the given lines, so the cause stays general. The message has no line number and the README has no entry for it. Because ParseCsolution returns false immediately after this message, any earlier error from ParseTargetTypes would appear alongside it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:94-97`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:86-87`
