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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The generator ID used in the taxonomy is not defined. Define or correct the generator ID ([/package/taxonomy element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_taxonomy.html))."
summary: "The PDSC /package/taxonomy contains a component or bundle entry whose generator attribute names a generator ID (%GENID%) that is not defined by any generator element in the package. packchk reports the taxonomy entry by its Cclass and Cgroup (%CCLASS%, …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; source clone unavailable)"]
---

## Symptom

`M361`
`Generator ID in Taxonomy 'Cclass=%CCLASS%, Cgroup=%CGROUP%' is undefined: '%GENID%'`

## Cause

The PDSC /package/taxonomy contains a component or bundle entry whose generator attribute names a generator ID (%GENID%) that is not defined by any generator element in the package. packchk reports the taxonomy entry by its Cclass and Cgroup (%CCLASS%, %CGROUP%) and the unresolved generator ID.

## Fix

Check the taxonomy element for the Cclass/Cgroup pair named in the message and make its generator attribute match an existing generator ID, or add the missing generator definition to the PDSC; then rerun packchk.

## Note

Answered from the message text and README only, since the source lines were not available; the trigger condition is inferred from the message wording and not verified in the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; source clone unavailable)`
