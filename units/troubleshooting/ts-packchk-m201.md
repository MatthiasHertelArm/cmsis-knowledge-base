---
id: "ts-packchk-m201"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M201: Error adding PDSC input file '…'!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M201"
symptoms: ["M201", "Error adding PDSC input file '%PATH%'!"]
symptom_regex: "^Error adding PDSC input file '.+?'!$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:85", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:94-99", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:125-128", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:106-113", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmltree/src/XMLTree.cpp:133-145"]
---

## Symptom

`M201`
`Error adding PDSC input file '%PATH%'!`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

M201 is logged when the XML reader refuses to register the PDSC (CreateModel.cpp:125-126), but RteModelReader::AddFile only fails for an empty name, which AddPdsc already rejects with M202, and XMLTree::AddFileName returns true when it does not parse. The message cannot occur at 30f5e81, so no PDSC cause can be named.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:85`
- `tools/packchk/src/CreateModel.cpp:94-99`
- `tools/packchk/src/CreateModel.cpp:125-128`
- `tools/packchk/src/RteModelReader.cpp:106-113`
- `libs/xmltree/src/XMLTree.cpp:133-145`
