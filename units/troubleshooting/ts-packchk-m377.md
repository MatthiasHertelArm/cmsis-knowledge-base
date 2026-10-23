---
id: "ts-packchk-m377"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M377: File '…' … must have 'attr=\"config\"'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M377"
symptoms: ["M377", "File '%NAME%' %TYPE% must have 'attr=\"config\"'"]
symptom_regex: "^File '.+?' .+? must have 'attr=\"config\"'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The category _'TYPE'_ of the file _'NAME'_ requires it to be defined as a configuration file. Add the attribute attr=\"config\" to the `<file>` element that defines the file. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "In a Device:Startup component (Cclass=\"Device\" Cgroup=\"Startup\"), a startup_* file or a system_*.c file of category source, sourceAsm or sourceC lacks attr=\"config\". %TYPE% shows the category."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:196", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:674-758", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:215"]
---

## Symptom

`M377`
`File '%NAME%' %TYPE% must have 'attr="config"'`

## Cause

In a Device:Startup component (Cclass="Device" Cgroup="Startup"), a startup_* file or a system_*.c file of category source, sourceAsm or sourceC lacks attr="config". %TYPE% shows the category.

## Fix

Add attr="config" and a version to these files, e.g. <file category="sourceC" attr="config" name="Source/system_ARMCM4.c" version="1.0.0"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:196`
- `tools/packchk/src/ValidateSemantic.cpp:674-758`
- `tools/packchk/README.md:215`
