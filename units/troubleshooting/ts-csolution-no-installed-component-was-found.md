---
id: "ts-csolution-no-installed-component-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed component was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed component was found"]
symptom_regex: "^no installed component was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4466"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution list components command (ListComponents) ran for a context with no device selected (empty selectedContext, i.e. no target-device context was named) and the active target's filtered component set came back empty."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4447-4469", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4466"]
---

## Symptom

`no installed component was found`

## Cause

The csolution list components command (ListComponents) ran for a context with no device selected (empty selectedContext, i.e. no target-device context was named) and the active target's filtered component set came back empty. That means none of the installed packs provided components that match the project's filters for that unnamed context. The message is the no-device counterpart of 'no component was found for device', which is printed when a device context is named.

## Fix

Check that the packs providing the components are installed and visible to csolution (for example with cpackget list or by checking the pack root), and that the csolution project's packs and target settings select a device/board whose packs are present. If you want the list for a specific device, name that context on the command line so the device-specific message is shown and the device's packs can be inspected.

## Trigger in the source

```cpp
if (!selectedContext.empty()) {
```

## Note

The message is printed only when selectedContext is empty; the trigger line 4466 is the else branch of that check. The README does not document this message. The exact reason the filtered set is empty is not visible in the lines given, so the cause above is an inference from the branch structure.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4447-4469`
- `tools/projmgr/src/ProjMgrWorker.cpp:4466`
