---
id: "ts-svdconv-m360"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M360: Address Block: found <…> (…) > …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M360"
symptoms: ["M360", "Address Block: found <%TAG%> (%HEXNUM%) > %HEXNUM2%."]
symptom_regex: "^Address Block: found <.+?> \\(.+?\\) > .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found an address block whose size or offset value (shown as the hexadecimal number in the message) is larger than the second hexadecimal value shown after the '>' sign, so the address block may extend beyond the range …"
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M360`
`Address Block: found <%TAG%> (%HEXNUM%) > %HEXNUM2%.`

## Cause

svdconv found an address block whose size or offset value (shown as the hexadecimal number in the message) is larger than the second hexadecimal value shown after the '>' sign, so the address block may extend beyond the range it is expected to occupy. The %TAG% in the message names the XML element concerned, and the two hex numbers are the value found and the limit it exceeds. The exact check could not be confirmed from source because the clone was not available.

## Fix

Open the SVD file at the element named in the message and compare the address block offset and size with the peripheral or register range it belongs to; correct the offset or size so that it fits within the expected range, then rerun svdconv.

## Note

The source lines were not available, so the trigger condition is inferred from the message text only. Verify the comparison direction and the meaning of each hexadecimal value in SVDConv_Msgs.cpp before relying on this entry.
