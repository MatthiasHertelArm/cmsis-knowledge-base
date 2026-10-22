---
id: "ts-packchk-m368"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M368: Cannot check '…'…"
status: "draft"
tool: "packchk"
severity: "error"
code: "M368"
symptoms: ["M368", "Cannot check '%NAME%'%MSG%"]
symptom_regex: "^Cannot check '.+?'.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this when it could not run its check on a named item, '%NAME%', and the optional '%MSG%' suffix carries the reason."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M368`
`Cannot check '%NAME%'%MSG%`

## Cause

packchk prints this when it could not run its check on a named item, '%NAME%', and the optional '%MSG%' suffix carries the reason. The item is probably a file or pack entry that could not be read or parsed, but the source lines were not available, so the exact trigger is not confirmed here.

## Fix

Read the detail text after the message, which is the reason packchk gives. Check that the named file or pack entry exists at the path shown and is well-formed, then rerun packchk on the pack.

## Note

Source lines were not available, so the trigger is inferred from the message text alone. The README does not document M368. The cause and fix above are a guess and should be verified against the source before use.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
