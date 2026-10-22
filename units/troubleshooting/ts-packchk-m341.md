---
id: "ts-packchk-m341"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M341: File with '…' dependency must have extension '…': '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M341"
symptoms: ["M341", "File with '%COMP%' dependency must have extension '%EXT%': '%PATH%'"]
symptom_regex: "^File with '.+?' dependency must have extension '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The file _'PATH'_ with dependency on component _'COMP'_ must have a specific extension _'EXT'_. Verify the dependency and correct the file extension. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "An assembler file (category sourceAsm, or category source with extension .s or .asm) has a condition that requires or accepts Tcompiler=\"GCC\", and its extension is lowercase .s; packchk asks for uppercase .S for GCC."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:159", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:394-398", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:758-803", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:182"]
---

## Symptom

`M341`
`File with '%COMP%' dependency must have extension '%EXT%': '%PATH%'`

## Cause

An assembler file (category sourceAsm, or category source with extension .s or .asm) has a condition that requires or accepts Tcompiler="GCC", and its extension is lowercase .s; packchk asks for uppercase .S for GCC.

## Fix

Rename the file to .S and update its name attribute, e.g. name="Source/GCC/startup_device.S".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:159`
- `tools/packchk/src/CheckFiles.cpp:394-398`
- `tools/packchk/src/CheckFiles.cpp:758-803`
- `tools/packchk/README.md:182`
