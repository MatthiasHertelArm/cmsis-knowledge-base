---
id: "ts-packchk-m317"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M317: Condition '…': No component found for '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M317"
symptoms: ["M317", "Condition '%NAME%': No component found for '%NAME2%'"]
symptom_regex: "^Condition '.+?': No component found for '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk checks a PDSC condition that refers to a component, and the component named in the condition's component reference could not be matched against any component the pack declares."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available in this session)"]
---

## Symptom

`M317`
`Condition '%NAME%': No component found for '%NAME2%'`

## Cause

packchk checks a PDSC condition that refers to a component, and the component named in the condition's component reference could not be matched against any component the pack declares. The message names the condition (%NAME%) and the component reference it could not resolve (%NAME2%). The likely input is a condition whose Cclass/Cgroup/Csub (or Cvendor/Cversion) does not match any <component> entry in the same PDSC.

## Fix

Open the PDSC file, find the <condition> named in the message, and compare its component reference with the <component> elements of the pack. Correct the spelling or the Cclass/Cgroup/Csub values so they match an existing component, or add the missing <component> element if it was meant to exist.

## Note

Answered from the message text alone because the clone was not available; the exact trigger condition and the attribute checked are inferred, not read from the code. Not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available in this session)`
