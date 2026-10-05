---
id: "ts-packchk-m344"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M344: File shall have condition containing '…': '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M344"
symptoms: ["M344", "File shall have condition containing '%COND%': '%PATH%'"]
symptom_regex: "^File shall have condition containing '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "File definition for _'PATH'_ shall contain a condition _'COND'_. Add attribute condition with the _'COND'_ in the `<file>` tag that defines the _'PATH'_ file. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:162", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:386-398", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:689-751", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:810-833", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:185"]
---

## Symptom

`M344`
`File shall have condition containing '%COND%': '%PATH%'`

## Cause

A library or assembler file (category library or sourceAsm, or category source with extension .s or .asm) has no condition with a Tcompiler expression, neither on the <file> nor on its <component>. %COND% is always 'Tcompiler'.

## Fix

Add a condition that requires the compiler and attach it to the file or its component, e.g. <condition id="GCC"><require Tcompiler="GCC"/></condition> and <file category="sourceAsm" name="Source/GCC/startup.S" condition="GCC"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:162`
- `tools/packchk/src/CheckFiles.cpp:386-398`
- `tools/packchk/src/CheckFiles.cpp:689-751`
- `tools/packchk/src/CheckFiles.cpp:810-833`
- `tools/packchk/README.md:185`
