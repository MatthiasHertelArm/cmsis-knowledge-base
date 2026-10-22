---
id: "ts-svdconv-m305"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M305: Name not C compliant: '…' : …, replaced by '_'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M305"
symptoms: ["M305", "Name not C compliant: '%NAME%' : %HEX%, replaced by '_'"]
symptom_regex: "^Name not C compliant: '.+?' : .+?, replaced by '_'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a name in the SVD input that is not a valid C identifier, so it replaced the offending character with '_' when generating the output. %NAME% is the original name and %HEX% is the code of the …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M305`
`Name not C compliant: '%NAME%' : %HEX%, replaced by '_'`

## Cause

svdconv found a name in the SVD input that is not a valid C identifier, so it replaced the offending character with '_' when generating the output. %NAME% is the original name and %HEX% is the code of the character that was replaced. The name most likely comes from a peripheral, register, or field element in the SVD file that contains characters such as spaces, hyphens, or other non-identifier symbols.

## Fix

Rename the flagged element in the SVD file so that it uses only letters, digits and underscores and does not start with a digit, then run svdconv again. If the replaced name is acceptable, no action is needed beyond checking that the generated identifier is what you expect.

## Note

Source lines were not available, so the trigger and handling are inferred from the message text and the README description only. The message is printed with severity error, though replacement suggests it may be a warning in practice; verify the severity against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
