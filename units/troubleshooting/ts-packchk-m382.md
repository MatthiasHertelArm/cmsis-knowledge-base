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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The package requires a package with name _'NAME'_ and version _'VER'_ from vendor _'VENDOR'_."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:201", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:2019-2091", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:198-229", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:281-310", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:220"]
---

## Symptom

`M382`
`Requirement <%TAG%> '[%VENDOR%] %NAME% %VER%' could not be resolved.%MSG%. Use option -i PackName.pdsc to resolve external dependencies.`

## Cause

The package requires a package with name _'NAME'_ and version _'VER'_ from vendor _'VENDOR'_. That package was not found. Verify the requirement. Use option `-i` to point to the required package. Refer to [/package/requirements/packages](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html#element_packages).

## Fix

Pass the required pack's PDSC with -i (e.g. -i /path/to/ARM.CMSIS.pdsc), or correct vendor, name or the version range of the <package> entry in <requirements><packages>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:201`
- `tools/packchk/src/ValidateSyntax.cpp:2019-2091`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:198-229`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:281-310`
- `tools/packchk/README.md:220`
