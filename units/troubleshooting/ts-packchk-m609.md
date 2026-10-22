---
id: "ts-packchk-m609"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M609: Processor '…': Exact one memory with attribute \"startup=1\" must be configured, but found …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M609"
symptoms: ["M609", "Processor '%NAME%': Exact one memory with attribute \"startup=1\" must be configured, but found %NUM%"]
symptom_regex: "^Processor '.+?': Exact one memory with attribute \"startup=1\" must be configured, but found .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk checks the processor memory map of a device in the PDSC and counts the memory entries that carry the attribute startup=1."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; inferred from the message text)"]
---

## Symptom

`M609`
`Processor '%NAME%': Exact one memory with attribute "startup=1" must be configured, but found %NUM%`

## Cause

packchk checks the processor memory map of a device in the PDSC and counts the memory entries that carry the attribute startup=1. The warning says that the count for processor '%NAME%' is %NUM%, while exactly one such memory is required. Zero or more than one startup memory in the device's memory definitions triggers it.

## Fix

Open the PDSC device entry for the named processor and check its memory elements. Make sure exactly one memory has startup="1" (the one the device boots from), and that no other memory for that processor also sets startup="1". Then rerun packchk.

## Note

Source lines were not available, so the trigger condition is inferred from the message text only. The README does not document M609. Confirm the exact count check in PackChk_Msgs.cpp before relying on the wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; inferred from the message text)`
