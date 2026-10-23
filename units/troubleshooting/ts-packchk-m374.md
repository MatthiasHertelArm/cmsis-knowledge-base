---
id: "ts-packchk-m374"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M374: While checking Feature for '…': Pname '…' not found."
status: "draft"
tool: "packchk"
severity: "error"
code: "M374"
symptoms: ["M374", "While checking Feature for '%MCU%': Pname '%CPU%' not found."]
symptom_regex: "^While checking Feature for '.+?': Pname '.+?' not found\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The processor could not be found for the specified device. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) and [/package/devices/family/.../processor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_processor)."
summary: "A <feature> or <algorithm> of a device has a Pname that matches no <processor Pname> of that device, including processors inherited from family and subFamily."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:193", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:868-928", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:587-611", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteDevice.cpp:602-609", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:212"]
---

## Symptom

`M374`
`While checking Feature for '%MCU%': Pname '%CPU%' not found.`

## Cause

A <feature> or <algorithm> of a device has a Pname that matches no <processor Pname> of that device, including processors inherited from family and subFamily.

## Fix

Correct Pname to one of the device's processor names, or add the missing <processor Pname="..."> definition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:193`
- `tools/packchk/src/ValidateSyntax.cpp:868-928`
- `tools/packchk/src/ValidateSyntax.cpp:587-611`
- `libs/rtemodel/src/RteDevice.cpp:602-609`
- `tools/packchk/README.md:212`
