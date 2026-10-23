---
id: "ts-packchk-m381"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M381: Vendor names are not equal: '[…] …', MCU '[…] …', see Line …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M381"
symptoms: ["M381", "Vendor names are not equal: '[%VENDOR%] %MCU%', MCU '[%VENDOR2%] %MCU2%', see Line %LINE%"]
symptom_regex: "^Vendor names are not equal: '\\[.+?\\] .+?', MCU '\\[.+?\\] .+?', see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Vendor name specified in the Dvendor attribute for the `<mountedDevice>` tag does not match the actual device vendor name. Verify and correct vendor name. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice)."
summary: "The Dvendor of a <mountedDevice> or <compatibleDevice> identifies the device's vendor but is not written the same way as the Dvendor of the device itself (e.g."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:200", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1751-1759", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1800-1808", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteModel.cpp:682-698", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/DeviceVendor.cpp:382-396", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:219"]
---

## Symptom

`M381`
`Vendor names are not equal: '[%VENDOR%] %MCU%', MCU '[%VENDOR2%] %MCU2%', see Line %LINE%`

## Cause

The Dvendor of a <mountedDevice> or <compatibleDevice> identifies the device's vendor but is not written the same way as the Dvendor of the device itself (e.g. "ARM" versus "ARM:82"), or it is empty.

## Fix

Copy the Dvendor value exactly as the device's family defines it, e.g. Dvendor="ARM:82".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:200`
- `tools/packchk/src/ValidateSyntax.cpp:1751-1759`
- `tools/packchk/src/ValidateSyntax.cpp:1800-1808`
- `libs/rtemodel/src/RteModel.cpp:682-698`
- `libs/rteutils/src/DeviceVendor.cpp:382-396`
- `tools/packchk/README.md:219`
