---
id: "ts-csolution-has-case-inconsistency-use"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' has case inconsistency, use '…' instead"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' has case inconsistency, use '<…>' instead"]
symptom_regex: "^'.+?' has case inconsistency, use '.+?' instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:347"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "EnsurePortability resolves a relative path from a csolution YAML file against the file's parent directory, and if that path exists it compares the lexically normalized form with the filesystem's canonical spelling."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:333-353", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:343-348"]
---

## Symptom

`'<…>' has case inconsistency, use '<…>' instead`

## Cause

EnsurePortability resolves a relative path from a csolution YAML file against the file's parent directory, and if that path exists it compares the lexically normalized form with the filesystem's canonical spelling. When the two differ, the path in the YAML uses different letter case from the actual file or directory on disk, which is not portable to case-sensitive systems. The first placeholder is the value as written in the YAML and the second is the canonical path relative to the parent directory.

## Fix

Edit the path in the csolution YAML so its letter case matches the file or directory name on disk, using the suggested relative path from the message, for example replacing a path written as Src/Main.c with src/main.c if the disk name is src/main.c. Then rebuild.

## Trigger in the source

```cpp
if (!canonical.empty() && (original != canonical)) {
```

## Note

The check runs only when the path exists, so a missing file produces no case warning. The same EnsurePortability function also emits the backslash and absolute-path warnings, which are separate messages.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:333-353`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:343-348`
