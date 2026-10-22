---
id: "ts-csolution-customization-of-intermediate-directory-intdir-i"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend"]
symptom_regex: "^customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:204"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution YAML sets an intermediate directory (`directories: intdir:`) at the solution level, but the build is running with the cbuild2cmake backend (m_cbuild2cmake is set)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:194-195", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:202-204", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:205-207"]
---

## Symptom

`customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend`

## Cause

The csolution YAML sets an intermediate directory (`directories: intdir:`) at the solution level, but the build is running with the cbuild2cmake backend (m_cbuild2cmake is set). In AddContext the cbuild2cmake path keeps the default intdir of 'tmp' and only emits this warning instead of applying the user's 'intdir' value, so the customization has no effect on the generated context.

## Fix

Remove the `intdir` entry from the `directories` section of the csolution file if the default intermediate directory is acceptable, or build without the cbuild2cmake backend if the custom 'intdir' must be honoured. The source only shows that the value is ignored; it does not show another supported way to set it under cbuild2cmake.

## Trigger in the source

```cpp
if (m_cbuild2cmake) {
```

## Note

The README does not document this message. The warning fires once per context created while the csolution intdir is non-empty, so it can repeat for each build-type and target-type combination in the log.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:194-195`
- `tools/projmgr/src/ProjMgrWorker.cpp:202-204`
- `tools/projmgr/src/ProjMgrWorker.cpp:205-207`
