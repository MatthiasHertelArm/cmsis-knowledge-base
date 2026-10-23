---
id: "ts-packchk-m347"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M347: Generator ID in Component 'Cclass=…, Cgroup=…, Cversion=…' is undefined: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M347"
symptoms: ["M347", "Generator ID in Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is undefined: '%GENID%'"]
symptom_regex: "^Generator ID in Component 'Cclass=.+?, Cgroup=.+?, Cversion=.+?' is undefined: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The generator ID used in the component could not be found."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:165", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckComponents.cpp:113-145", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1822-1881", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:188"]
---

## Symptom

`M347`
`Generator ID in Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is undefined: '%GENID%'`

## Cause

The generator ID used in the component could not be found. Verify and correct the generator ID ([/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)), or define the generator ID (ref [/package/generators/generator](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html#element_generator)).

## Fix

Define the generator in the same PDSC, <generators><generator id="MyGenerator">...</generator></generators>, or correct the component's generator attribute to an existing generator id.

## Note

The component check is skipped when the pack has no <generators> element (CheckComponents.cpp:121-122). The taxonomy check compares the generator attribute of the <taxonomy> element rather than that of each <description> and reports M347, not M361 (ValidateSyntax.cpp:1834-1870).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:165`
- `tools/packchk/src/CheckComponents.cpp:113-145`
- `tools/packchk/src/ValidateSyntax.cpp:1822-1881`
- `tools/packchk/README.md:188`
