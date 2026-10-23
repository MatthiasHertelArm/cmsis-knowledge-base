---
id: "ts-packchk-m361"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M361: Generator ID in Taxonomy 'Cclass=…, Cgroup=…' is undefined: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M361"
symptoms: ["M361", "Generator ID in Taxonomy 'Cclass=%CCLASS%, Cgroup=%CGROUP%' is undefined: '%GENID%'"]
symptom_regex: "^Generator ID in Taxonomy 'Cclass=.+?, Cgroup=.+?' is undefined: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The generator ID used in the taxonomy is not defined."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:180", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:62", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1822-1881", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:200"]
---

## Symptom

`M361`
`Generator ID in Taxonomy 'Cclass=%CCLASS%, Cgroup=%CGROUP%' is undefined: '%GENID%'`

## Cause

The generator ID used in the taxonomy is not defined. Define or correct the generator ID ([/package/taxonomy element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_taxonomy.html)).

## Fix

Define the generator in <generators><generator id="..."> of the same PDSC, or correct the generator attribute of the taxonomy <description>.

## Note

No raise site for M361 at 30f5e81: CheckTaxonomy reports an undefined generator as M347, and it only runs when the <taxonomy> element itself has a generator attribute (ValidateSyntax.cpp:1834-1870). Fix inferred from the message and README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:180`
- `tools/packchk/src/PackChk_Msgs.cpp:62`
- `tools/packchk/src/ValidateSyntax.cpp:1822-1881`
- `tools/packchk/README.md:200`
