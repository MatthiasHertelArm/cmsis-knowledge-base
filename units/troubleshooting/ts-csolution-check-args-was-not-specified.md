---
id: "ts-csolution-check-args-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: check <args> was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["check <args> was not specified"]
symptom_regex: "^check <args> was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:451"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution command was invoked as 'check' with no argument after it, so the internal argument string m_args is empty when ProcessCheckCommand runs."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:450-453", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:455-457", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:458-462"]
---

## Symptom

`check <args> was not specified`

## Cause

The csolution command was invoked as 'check' with no argument after it, so the internal argument string m_args is empty when ProcessCheckCommand runs. The only accepted argument in the handler table is 'pack-updates'.

## Fix

Run the check command with its argument, for example: csolution check pack-updates [options]. Run csolution help or the csolution documentation to confirm the accepted check subcommand spelling for your version.

## Trigger in the source

```cpp
if (m_args.empty()) {
```

## Note

The same pattern is used by ProcessListCommand (ProjMgr.cpp:415-418) with 'list <args> was not specified'. The README does not document this message. The lines show only the 'pack-updates' handler, so that is the only valid argument visible here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:450-453`
- `tools/projmgr/src/ProjMgr.cpp:455-457`
- `tools/projmgr/src/ProjMgr.cpp:458-462`
