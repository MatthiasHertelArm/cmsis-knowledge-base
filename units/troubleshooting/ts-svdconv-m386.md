---
id: "ts-svdconv-m386"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M386: Name not C compliant: '…' : Brackets [] found"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M386"
symptoms: ["M386", "Name not C compliant: '%NAME%' : Brackets [] found"]
symptom_regex: "^Name not C compliant: '.+?' : Brackets \\[\\] found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this when a name taken from the SVD input (a peripheral, register, field or similar identifier) contains square brackets, which are not allowed in a C identifier."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M386`
`Name not C compliant: '%NAME%' : Brackets [] found`

## Cause

svdconv prints this when a name taken from the SVD input (a peripheral, register, field or similar identifier) contains square brackets, which are not allowed in a C identifier. The %NAME% placeholder is the offending SVD name, typically an array-style name such as one with '[' and ']' characters left in it, so the generated C header would not compile.

## Fix

Find the element named in the message in the SVD file and rename it so it contains only letters, digits and underscores, for example replacing '[' and ']' with '_'. Then rerun svdconv on the corrected SVD file.

## Note

Only the message text was available; the trigger condition was not checked against the source lines, so the cause is inferred from the message wording and should be verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
