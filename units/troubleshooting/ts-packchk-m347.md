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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The generator ID used in the component could not be found. Verify and correct the generator ID ([/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)), or define the generator ID (ref [/package/generators/generator](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html#element_generator))."
summary: "The component in the PDSC refers to a generator ID (the generator attribute on a component, or a generator reference) that does not match any <generator> element with that Id in the package."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M347`
`Generator ID in Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is undefined: '%GENID%'`

## Cause

The component in the PDSC refers to a generator ID (the generator attribute on a component, or a generator reference) that does not match any <generator> element with that Id in the package. The %GENID% is the ID the component uses, and the %CCLASS%, %CGROUP% and %CVER% identify the component that carries it. The source lines were not available, so this follows the README and the message text only.

## Fix

Check the generator attribute of the named component in the PDSC and make it match the Id of a <generator> element defined in the same package, correcting the spelling if needed. If the generator is missing, add a <generators> section with a <generator Id="..."> element for that ID.

## Note

Source lines were not provided, so the trigger condition is inferred from the message text and README rather than read from code. The README gives the same cause and fix, so it was not contradicted.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
