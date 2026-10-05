---
id: "ts-packchk-m388"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M388: Unsupported character(s) found in '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M388"
symptoms: ["M388", "Unsupported character(s) found in '%NAME%'"]
symptom_regex: "^Unsupported character\\(s\\) found in '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:207", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:222-230", "Open-CMSIS-Pack/devtools@30f5e817:libs/xmlreader/src/XML_Reader.cpp:515-527", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:915-950", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestTextExceedsLength/TestVendor.TestTextExceedsLength.pdsc:28"]
---

## Symptom

`M388`
`Unsupported character(s) found in '%NAME%'`

## Cause

The text of a <description> element contains a character outside printable US-ASCII (0x20 to 0x7E), for example a non-ASCII letter, a symbol such as the euro sign, typographic quotes, or a line break inside the text; %NAME% shows the whole description.

## Fix

Replace such characters with plain ASCII (e.g. 'EUR', straight quotes) and keep the description on one line.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:207`
- `tools/packchk/src/CheckFiles.cpp:222-230`
- `libs/xmlreader/src/XML_Reader.cpp:515-527`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:915-950`
- `tools/packchk/test/data/TestTextExceedsLength/TestVendor.TestTextExceedsLength.pdsc:28`
