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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The processor could not be found for the specified device. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) and [/package/devices/family/.../processor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_processor)."
summary: "packchk checks a device's Feature entries against the processors declared for that device."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available in this review)"]
---

## Symptom

`M374`
`While checking Feature for '%MCU%': Pname '%CPU%' not found.`

## Cause

packchk checks a device's Feature entries against the processors declared for that device. The message is printed when a Feature element names a processor (Pname) for the device %MCU% that does not match any processor declared for it in the PDSC. The %CPU% in the message is the Pname value that could not be resolved. The README points to the device and processor elements of the PDSC family description, which is where the matching processor name has to be declared.

## Fix

Open the PDSC file that defines the device and compare the Pname attribute of the Feature element with the Pname attributes of the processor elements under that device (or its family). Correct the Pname so it matches a declared processor, or add the missing processor element to the device. Then run packchk again.

## Note

Cause and fix are read from the message text and the README, since the source clone was not available to confirm the trigger condition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available in this review)`
