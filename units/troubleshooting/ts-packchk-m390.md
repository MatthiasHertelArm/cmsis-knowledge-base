---
id: "ts-packchk-m390"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M390: Condition '…': Direct or indirect recursion detected. …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M390"
symptoms: ["M390", "Condition '%NAME%': Direct or indirect recursion detected. %MSG%"]
symptom_regex: "^Condition '.+?': Direct or indirect recursion detected\\. .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The packchk condition check found a cycle while resolving the condition named in the message."
cause_origin: "source-analysis"
confidence: "low"
---

## Symptom

`M390`
`Condition '%NAME%': Direct or indirect recursion detected. %MSG%`

## Cause

The packchk condition check found a cycle while resolving the condition named in the message. The condition '%NAME%' references itself, either directly or through a chain of other conditions, so its evaluation would never finish. The %MSG% part is the checker's detail text and may name the conditions involved in the loop. The source trigger was not available, so this reading comes from the message text alone.

## Fix

Open the PDSC file and find the condition with the id given in the message. Follow the condition references it makes, such as those in its require, accept or deny children, through the other conditions they point to. Remove or redirect the reference that closes the loop so that no condition depends on itself, directly or indirectly, then re-run packchk.

## Note

The clone was not available, so no source lines were checked and the trigger condition is not confirmed. The README does not document M390. The cause and fix describe the usual reading of a condition cycle and should be checked against tools/packchk/src/PackChk_Msgs.cpp before relying on them.
