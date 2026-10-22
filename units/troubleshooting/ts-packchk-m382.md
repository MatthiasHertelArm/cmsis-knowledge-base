---
id: "ts-packchk-m382"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M382: Requirement <…> '[…] … …' could not be resolved.…. Use option -i PackName.pdsc to resolve external …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M382"
symptoms: ["M382", "Requirement <%TAG%> '[%VENDOR%] %NAME% %VER%' could not be resolved.%MSG%. Use option -i PackName.pdsc to resolve external dependencies."]
symptom_regex: "^Requirement <.+?> '\\[.+?\\] .+? .+?' could not be resolved\\..+?\\. Use option \\-i PackName\\.pdsc to resolve external dependencies\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The package requires a package with name _'NAME'_ and version _'VER'_ from vendor _'VENDOR'_. That package was not found. Verify the requirement. Use option `-i` to point to the required package. Refer to [/package/requirements/packages](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html#element_packages)."
summary: "packchk checks the requirements of the package it validates, the packages, components or APIs a PDSC lists under requirements."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)"]
---

## Symptom

`M382`
`Requirement <%TAG%> '[%VENDOR%] %NAME% %VER%' could not be resolved.%MSG%. Use option -i PackName.pdsc to resolve external dependencies.`

## Cause

packchk checks the requirements of the package it validates, the packages, components or APIs a PDSC lists under requirements. For a requirement whose tag is shown in place of %TAG%, the named package (vendor %VENDOR%, name %NAME%, version %VER%) could not be found among the packages it can see, so the requirement stays unresolved. The optional %MSG% part adds detail about why the lookup failed.

## Fix

Check that the requirement in the PDSC matches an installed or available package by vendor, name and version. If the required pack lives outside the set packchk scans, pass its PDSC with -i PackName.pdsc so the requirement can be resolved.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and README, not read from code. The README says to 'Verify the requirement' and to use -i; the message itself gives the same -i hint, so the fix matches. The README uses 'option -i' while the message names -i PackName.pdsc, consistent with each other.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)`
