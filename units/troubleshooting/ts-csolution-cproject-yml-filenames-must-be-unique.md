---
id: "ts-csolution-cproject-yml-filenames-must-be-unique"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject.yml filenames must be unique"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject.yml filenames must be unique"]
symptom_regex: "^cproject\\.yml filenames must be unique$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:517"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution file lists more than one cproject in its projects section, and two or more of those entries end in the same file name (for example two entries both pointing at a cproject.yml in different directories)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:508-519"]
---

## Symptom

`cproject.yml filenames must be unique`

## Cause

The csolution file lists more than one cproject in its projects section, and two or more of those entries end in the same file name (for example two entries both pointing at a cproject.yml in different directories). The tool collects only the file name of each listed cproject, sorts them, and fails when any name appears twice. Such a solution cannot be processed because the resulting project names would collide.

## Fix

Rename the cproject.yml files so that each file name is unique across the solution, for example by giving each project a distinct file name such as app1.cproject.yml and app2.cproject.yml, and update the matching entries under projects in the csolution.yml. Keep each project in its own sub-directory as well, since the tool warns when directories are shared.

## Trigger in the source

```cpp
if (adjacent_find(names.begin(), names.end()) != names.end()) {
```

## Note

The message is printed with the csolution file as its file argument. The check compares only file names, so two projects in different directories with the same file name also trigger it; the directory check at line 520 only produces a warning. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:508-519`
