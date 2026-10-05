---
id: "ts-packchk-m357"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M357: Config File '…', which gets copied to project, is also found in the include path to the original …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M357"
symptoms: ["M357", "Config File '%NAME%', which gets copied to project, is also found in the include path to the original pack folder. Do not place config header files in the same directory as regular header files. See Line %LINE%"]
symptom_regex: "^Config File '.+?', which gets copied to project, is also found in the include path to the original pack folder\\. Do not place config header files in the same directory as regular header files\\. See Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:175", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:913-963", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:684-690", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:766-774", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:886-913", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/ConfigFileInIncludePath/TestVendor.ConfigFileInIncludePathPack.pdsc:60-70"]
---

## Symptom

`M357`
`Config File '%NAME%', which gets copied to project, is also found in the include path to the original pack folder. Do not place config header files in the same directory as regular header files. See Line %LINE%`

## Cause

A configuration file (<file attr="config">) sits in a folder that the pack also uses as include path, either a <file category="include"> folder or the folder of a <file category="header">. A project then sees both its own copy and the original in the pack; %LINE% points to the entry that adds the include path.

## Fix

Move config files into their own folder (e.g. Config/) that no include or header entry points to and update their name attributes; keep regular headers in the include folder.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:175`
- `tools/packchk/src/CheckFiles.cpp:913-963`
- `tools/packchk/src/ValidateSemantic.cpp:684-690`
- `tools/packchk/src/ValidateSemantic.cpp:766-774`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:886-913`
- `tools/packchk/test/data/ConfigFileInIncludePath/TestVendor.ConfigFileInIncludePathPack.pdsc:60-70`
