---
id: "ts-csolution-it-must-be-latest-all-or-required"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: unknown load option: '…', it must be 'latest', 'all' or 'required'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["unknown load option: '<…>', it must be 'latest', 'all' or 'required'"]
symptom_regex: "^unknown load option: '.+?', it must be 'latest', 'all' or 'required'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:478"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution tool was given a load-packs policy value (from the command-line option that sets m_loadPacksPolicy) that is none of the accepted keywords."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:468-482"]
---

## Symptom

`unknown load option: '<…>', it must be 'latest', 'all' or 'required'`

## Cause

The csolution tool was given a load-packs policy value (from the command-line option that sets m_loadPacksPolicy) that is none of the accepted keywords. SetLoadPacksPolicy accepts an empty value (default policy), 'latest', 'all' or 'required' and maps each to a LoadPacksPolicy; any other string falls through to the error, which prints the rejected value in place of the placeholder.

## Fix

Re-run the command with the load option set to one of the accepted values: 'latest', 'all' or 'required'. Check the spelling and case of the value passed to the option, and omit the option to get the default policy.

## Trigger in the source

```cpp
} else if (m_loadPacksPolicy == "required") {
```

## Note

The trigger line shown is one branch of the chain; the error itself is at ProjMgr.cpp:478. The option name that carries the value is not visible in the given lines, so the exact command-line flag is not stated here. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:468-482`
