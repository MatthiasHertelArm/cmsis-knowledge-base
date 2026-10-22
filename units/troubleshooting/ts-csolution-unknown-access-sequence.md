---
id: "ts-csolution-unknown-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: unknown access sequence: '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["unknown access sequence: '<…>'"]
symptom_regex: "^unknown access sequence: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3783"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The text between the dollar-sign delimiters (the '<…>' in the message) is an access sequence that matches neither the pack-directory form nor the accessSequencesRegEx form, so the tool cannot expand it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3727-3730", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3781-3784"]
---

## Symptom

`unknown access sequence: '<…>'`

## Cause

The text between the dollar-sign delimiters (the '<…>' in the message) is an access sequence that matches neither the pack-directory form nor the accessSequencesRegEx form, so the tool cannot expand it. The sequence was found in a path-like value of the csolution or its layers, and the failed match at this line is the only place the error is printed. The exact accepted spellings are defined by the regexes, which are not among the lines given.

## Fix

Find the quoted sequence in the csolution YAML or layer file and correct its spelling so it matches a supported access sequence form, including the optional context argument. Check the README or the access sequence documentation for the supported names. If the sequence was meant as literal text, remove or escape the dollar signs.

## Note

The supported sequence names and the regex definitions were not in the lines provided, so the fix stays general. The message is printed only in the else branch after both regex checks fail, so it is reachable for any sequence that does not match either form.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3727-3730`
- `tools/projmgr/src/ProjMgrWorker.cpp:3781-3784`
