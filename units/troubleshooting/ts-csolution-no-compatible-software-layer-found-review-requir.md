---
id: "ts-csolution-no-compatible-software-layer-found-review-requir"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no compatible software layer found. Review required connections of the project"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no compatible software layer found. Review required connections of the project"]
symptom_regex: "^no compatible software layer found\\. Review required connections of the project$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:1016"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list layers` could not complete layer discovery for the context named with the message."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1012", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4938", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2334", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2466", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2543"]
---

## Symptom

`no compatible software layer found. Review required connections of the project`

## Cause

`csolution list layers` could not complete layer discovery for the context named with the message. Mostly no combination of clayer.yml files (from the loaded packs or from `-L`/`--clayer-path`) provides the `connections:` that the project and its layers consume; the lines before it list the connection checks. Earlier failures for the context (pack loading, a `-L` path that does not exist, undefined layer variables) end with the same message.

## Fix

Read the connection report printed before the message (add `-v` or `-d` for detail). Install the board or device pack that ships a matching layer, point `-L` to a folder with compatible clayer.yml files, or adjust the `connections:` the project consumes; fix any earlier error first.

## Trigger in the source

```cpp
if (!m_worker.ListLayers(layers, m_clayerSearchPath, m_failedContext)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1012`
- `tools/projmgr/src/ProjMgrWorker.cpp:4938`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2334`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2466`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2543`
