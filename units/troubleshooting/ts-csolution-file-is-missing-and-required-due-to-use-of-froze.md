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
summary: "`--frozen-packs` was given, but the pack lock file `<name>.cbuild-pack.yml` next to the csolution.yml does not exist; frozen packs require it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:59-68", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1336-1351"]
---

## Symptom

`file is missing and required due to use of --frozen-packs option`

## Cause

`--frozen-packs` was given, but the pack lock file `<name>.cbuild-pack.yml` next to the csolution.yml does not exist; frozen packs require it. The message is prefixed with the expected file path.

## Fix

Run once without `--frozen-packs` to create the cbuild-pack.yml, commit it, and use `--frozen-packs` afterwards (e.g. in CI).

## Trigger in the source

```cpp
} else if (frozenPacks) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:59-68`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1336-1351`
