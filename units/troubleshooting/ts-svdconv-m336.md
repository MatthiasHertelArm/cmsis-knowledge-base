---
id: "ts-svdconv-m336"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M336: … '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M336"
symptoms: ["M336", "%LEVEL% '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file defines an element (such as a peripheral, register, or field) with a name that already appears earlier at the same level of the device description, so the name is not unique."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:M336 message text (trigger lines not available in this session)"]
---

## Symptom

`M336`
`%LEVEL% '%NAME%' already defined %LINE%`

## Cause

The SVD file defines an element (such as a peripheral, register, or field) with a name that already appears earlier at the same level of the device description, so the name is not unique. The message fills %LEVEL% with the kind of element, %NAME% with the duplicated name, and %LINE% with the location of the earlier definition.

## Fix

Open the SVD file at the line reported in the message and rename or remove the duplicate element so each peripheral name, and each register or field name within its parent, is unique. Then rerun svdconv. If the duplicate was introduced by a derived peripheral (derivedFrom), check that the copied name is changed to a distinct one.

## Note

Source lines were not available, so the cause is inferred from the message text and the README. The exact scope of uniqueness (device-wide for peripherals, per parent for registers and fields) was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:M336 message text (trigger lines not available in this session)`
