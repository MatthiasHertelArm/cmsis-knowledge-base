---
id: "ts-csolution-projects-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: projects not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["projects not found"]
symptom_regex: "^projects not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:505"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution file given to csolution has no projects: its `projects` list is empty and it also defines no `west-apps` and no `cmake-apps`."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:503-507", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:489-491"]
---

## Symptom

`projects not found`

## Cause

The csolution file given to csolution has no projects: its `projects` list is empty and it also defines no `west-apps` and no `cmake-apps`. The check runs when the solution is not an image-only build. The message is followed by the csolution file path, which is the file that lacks the project entries.

## Fix

Open the csolution.yml file named in the message and add at least one cproject entry under `projects:` (for example `- project: <path-to-project>/<name>.cproject.yml`, where the path is relative to the csolution file), or define a west or CMake application if that is the build style in use. Then run the command again.

## Trigger in the source

```cpp
if (!IsSolutionImageOnly() && cprojects.empty() && m_parser.GetCsolution().westApps.empty() && m_parser.GetCsolution().cmakeApps.empty()) {
```

## Note

The README does not document this message. The fix text describes the csolution YAML structure from the code's list names (cprojects, westApps, cmakeApps); the exact YAML key spelling was not verified against the parser in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:503-507`
- `tools/projmgr/src/ProjMgr.cpp:489-491`
