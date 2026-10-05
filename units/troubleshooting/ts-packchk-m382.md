---
id: "ts-packchk-m382"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M382: . Use option -i PackName.pdsc to resolve external dependencies."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M382"
symptoms: ["M382", "Requirement <%TAG%> '[%VENDOR%] %NAME% %VER%' could not be resolved.%MSG%. Use option -i PackName.pdsc to resolve external dependencies."]
symptom_regex: "^Requirement <.+?> '\\[.+?\\] .+? .+?' could not be resolved\\..+?\\. Use option \\-i PackName\\.pdsc to resolve external dependencies\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M382`
`Requirement <%TAG%> '[%VENDOR%] %NAME% %VER%' could not be resolved.%MSG%. Use option -i PackName.pdsc to resolve external dependencies.`

## Cause

The package requires a package with name _'NAME'_ and version _'VER'_ from vendor _'VENDOR'_. That package was not found. Verify the requirement. Use option `-i` to point to the required package. Refer to [/package/requirements/packages](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html#element_packages).

## Fix

_siehe Cause_
