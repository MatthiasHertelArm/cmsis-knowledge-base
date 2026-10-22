---
id: "ts-csolution-file-is-missing-and-required-due-to-use-of-froze"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file is missing and required due to use of --frozen-packs option"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file is missing and required due to use of --frozen-packs option"]
symptom_regex: "^file is missing and required due to use of \\-\\-frozen\\-packs option$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:66"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution tool was run with the --frozen-packs option, which requires the pack set to be fixed by an existing cbuild-pack file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:60-61", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:65-68"]
---

## Symptom

`file is missing and required due to use of --frozen-packs option`

## Cause

The csolution tool was run with the --frozen-packs option, which requires the pack set to be fixed by an existing cbuild-pack file. ParseCsolution derives the expected name by replacing the .csolution.yml suffix of the input with .cbuild-pack.yml; when that file does not exist and frozenPacks is set, the tool prints this error with that expected path as the file and stops. The file is missing because the packs have not been resolved and written to a cbuild-pack file yet, or the file is located elsewhere than the csolution file.

## Fix

Generate the cbuild-pack file next to the csolution file before running with --frozen-packs, for example by running the csolution command without --frozen-packs once (for instance a pack resolution or build run) so the cbuild-pack.yml is written, then rerun with --frozen-packs. Alternatively, drop --frozen-packs if you do not need a fixed pack set. Check that the file named in the message sits beside the .csolution.yml file.

## Trigger in the source

```cpp
} else if (frozenPacks) {
```

## Note

The message has no code and is not documented in the README. The fix to generate the cbuild-pack file by an earlier run is an inference from the source, since the source only checks for the file's existence; the source does not show which command writes it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:60-61`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:65-68`
