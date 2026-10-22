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
summary: "This message is printed by the list-layers command path (RunListLayers) when m_worker.ListLayers fails to detect a compatible software layer for at least one context."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1013-1018", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1001-1009"]
---

## Symptom

`no compatible software layer found. Review required connections of the project`

## Cause

This message is printed by the list-layers command path (RunListLayers) when m_worker.ListLayers fails to detect a compatible software layer for at least one context. It is emitted once per failed context, so the context name is attached as the second argument. The text itself does not name the layer or the connection; it only says the project's required connections need review, which points at the project's component selections or layer requirements not matching any available layer.

## Fix

Run the layer listing again on the csolution.yml and check the connections of each failed context: confirm that the components and layers required by the project are provided by the packs that are installed and referenced, and that the selected target/context matches what the layers were built for. Then rerun the command. The source gives no further automatic remedy, so review of the project's connections is the step to take.

## Trigger in the source

```cpp
if (!m_worker.ListLayers(layers, m_clayerSearchPath, m_failedContext)) {
```

## Note

The README does not document this message. The source only shows the trigger and the per-context reporting; the specific reasons ListLayers fails are not in the given lines, so the cause is an interpretation of the message text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1013-1018`
- `tools/projmgr/src/ProjMgr.cpp:1001-1009`
