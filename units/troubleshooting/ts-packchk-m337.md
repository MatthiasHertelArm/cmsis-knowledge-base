---
id: "ts-packchk-m337"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M337: File with category '…' has wrong extension '…': '…'…"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M337"
symptoms: ["M337", "File with category '%CAT%' has wrong extension '%EXT%': '%PATH%'%MSG%"]
symptom_regex: "^File with category '.+?' has wrong extension '.+?': '.+?'.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The extension of the file does not match the file category _'CAT'_ specified in the category attribute."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:155", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:840-911", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:322-332", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1078-1103", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:857-884", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:178"]
---

## Symptom

`M337`
`File with category '%CAT%' has wrong extension '%EXT%': '%PATH%'%MSG%`

## Cause

The extension of the file does not match the file category _'CAT'_ specified in the category attribute. Verify the extension to match the category. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

Use the extension that fits the category (header: .h or .hpp; sourceC: .c; sourceCpp: .cpp, .cc or .cxx; sourceAsm: .s or .asm; the package description overview: .md), or change category to match the file.

## Note

The overview attribute of <description> is not in the 1.7.15 schema copy in the tree (tools/packchk/test/data/schema.xsd).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:155`
- `tools/packchk/src/CheckFiles.cpp:840-911`
- `tools/packchk/src/ValidateSyntax.cpp:322-332`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1078-1103`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:857-884`
- `tools/packchk/README.md:178`
