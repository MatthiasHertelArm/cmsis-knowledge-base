---
id: "ts-csolution-is-deprecated-at-this-level-and-accepted-in-csol"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: …'device: Dname'…'board:' node… is deprecated at this level and accepted in *.csolution.yml only"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["<…>'device: Dname'<…>'board:' node<…> is deprecated at this level and accepted in *.csolution.yml only"]
symptom_regex: "^.+?'device: Dname'.+?'board:' node.+? is deprecated at this level and accepted in \\*\\.csolution\\.yml only$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:1127"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The board or device name is set under a target in a *.cproject.yml or *.clayer.yml file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1113-1114", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1119-1128"]
---

## Symptom

`<…>'device: Dname'<…>'board:' node<…> is deprecated at this level and accepted in *.csolution.yml only`

## Cause

The board or device name is set under a target in a *.cproject.yml or *.clayer.yml file. ParseTargetType collects the target's board and device values, and when the file name matches cproject or clayer yml, any non-empty value is reported, except a device written in the form :<processor-name>, which is silently accepted. The <…> placeholder is either the text 'device: Dname' or the 'board:' node, depending on which key is non-empty; the message prints the offending key name, not the value.

## Fix

Remove the board: or device: entry from the cproject.yml or clayer.yml file and move it to the *.csolution.yml file, where it is accepted. For a device that only selects a processor, write it in the form device: :<processor-name> so the warning is not raised.

## Trigger in the source

```cpp
if ((key == YAML_DEVICE) && regex_match(value, regex("^:[ -9;-~]+$"))) {
```

## Note

The message text has a variable part that differs per key: for device it is 'device: Dname' and for board it is 'board:' node. The placeholder <…> in the message is the same text used in the source. The source reports the warning once per non-empty key in each file, so both board and device can produce a warning in the same file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1113-1114`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1119-1128`
