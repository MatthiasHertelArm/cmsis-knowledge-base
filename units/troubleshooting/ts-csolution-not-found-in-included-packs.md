---
id: "ts-csolution-not-found-in-included-packs"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: component '…' not found in included packs… did you mean '…'?…"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["component '<…>' not found in included packs<…>\n  did you mean '<…>'?<…>"]
symptom_regex: "^component '.+?' not found in included packs.+?\\\n  did you mean '.+?'\\?.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2001"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution project lists a component in its components section (item.component) that does not match any component in the RTE target's filtered component set built from the packs the project includes."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1997-2003", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1983-1988"]
---

## Symptom

`component '<…>' not found in included packs<…>
  did you mean '<…>'?<…>`

## Cause

The csolution project lists a component in its components section (item.component) that does not match any component in the RTE target's filtered component set built from the packs the project includes. ProcessComponent looks up the requirement and returns no matched component; the hint, if any, is the closest name the matcher found. The '<…>' in the message is the component name from the YAML, and the optional 'did you mean' text is that hint.

## Fix

Compare the component name in the project's components section with the component list of the pack that provides it, and correct the spelling or use the hint shown. If the component comes from a pack that is not yet included, add that pack under packs in the project or the solution, then rebuild. Check that the pack is installed in the CMSIS pack root.

## Trigger in the source

```cpp
if (!matchedComponent) {
```

## Note

The message is printed in ProcessComponents with the hint appended; the same condition continues in rpc mode with an unresolved instance, and the error flag is still set. The exact mismatch rules are in ProcessComponent, which was not in the lines provided. No README entry exists for this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1997-2003`
- `tools/projmgr/src/ProjMgrWorker.cpp:1983-1988`
