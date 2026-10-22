---
id: "ts-csolution-improper-quotes"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: invalid define: …, improper quotes"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid define: <…>, improper quotes"]
symptom_regex: "^invalid define: .+?, improper quotes$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:450"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A define value in a csolution YAML file (the defines list of a project, component or similar node) contains double-quote characters that do not form a single correctly quoted pair."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:420-454", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:427-451"]
---

## Symptom

`invalid define: <…>, improper quotes`

## Cause

A define value in a csolution YAML file (the defines list of a project, component or similar node) contains double-quote characters that do not form a single correctly quoted pair. The validator counts the quotes in the value; if the count is not zero and not exactly two, or if the two quotes do not sit at both ends (either as a plain " ... " wrapper or as an escaped \" ... \" wrapper), the value is rejected. The <…> in the message is the define value as written in the YAML.

## Fix

Find the define named in the message and correct its quoting so that it has either no double quotes or exactly one pair wrapping the whole value, for example: defines: [ MY_STRING: "hello" ] (or a plain value without quotes). Remove stray or embedded quotes, or escape them so the value starts and ends with the quote pair. Then run the csolution command again.

## Trigger in the source

```cpp
if (!isValid) {
```

## Note

The message prints the whole define value; for map-style defines the value checked is the map value only, not the key. The check runs per define item and the function returns false, so the error is printed once per invalid value.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:420-454`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:427-451`
