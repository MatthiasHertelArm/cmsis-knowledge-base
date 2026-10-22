---
id: "ts-packchk-m608"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M608: Memory '…' with '…'='…' must have '…'='…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M608"
symptoms: ["M608", "Memory '%NAME%' with '%ATTR%'='%VALUE%' must have '%ATTR2%'='%VALUE2%'"]
symptom_regex: "^Memory '.+?' with '.+?'='.+?' must have '.+?'='.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The packchk check found a memory entry in a PDSC device definition whose attribute %ATTR% is set to %VALUE%, but the check requires the same entry to also carry %ATTR2% set to %VALUE2%."
cause_origin: "source-analysis"
confidence: "low"
---

## Symptom

`M608`
`Memory '%NAME%' with '%ATTR%'='%VALUE%' must have '%ATTR2%'='%VALUE2%'`

## Cause

The packchk check found a memory entry in a PDSC device definition whose attribute %ATTR% is set to %VALUE%, but the check requires the same entry to also carry %ATTR2% set to %VALUE2%. The memory is named %NAME%. This is inferred from the message text only, because the source lines around the trigger were not available.

## Fix

Open the PDSC device or memory definition that declares memory %NAME% and add or correct the attribute %ATTR2%=%VALUE2% on that entry, or change %ATTR%=%VALUE% if it was set in error. Then rerun packchk on the pack.

## Note

The clone was not available, so tools/packchk/src/PackChk_Msgs.cpp was not read and no line numbers are cited. The trigger condition and the exact pairing of attributes were not verified. The README does not document this message.
