---
id: "ts-packchk-m303"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M303: No package name found in the PDSC file. Add the <name> tag and provide the package name. For …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M303"
symptoms: ["M303", "No package name found in the PDSC file. Add the <name> tag and provide the package name. For example: <name>MCU-Name_DFP</name>."]
symptom_regex: "^No package name found in the PDSC file\\. Add the <name> tag and provide the package name\\. For example: <name>MCU\\-Name_DFP</name>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Package name is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<name>` and add the package name. For example `<name>MCU-Name_DFP</name>`. Refer to [/package/name](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_name)."
summary: "packchk found no <name> element under the root <package> element of the PDSC file, so the package has no name to identify it by."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)"]
---

## Symptom

`M303`
`No package name found in the PDSC file. Add the <name> tag and provide the package name. For example: <name>MCU-Name_DFP</name>.`

## Cause

packchk found no <name> element under the root <package> element of the PDSC file, so the package has no name to identify it by. The README states the same condition; the source lines were not available to confirm the exact check.

## Fix

Open the PDSC file and, directly inside the <package> element, add a <name> element holding the package name, for example <name>MCU-Name_DFP</name>, then run packchk again.

## Note

Source lines were not provided, so the trigger condition is taken from the message text and the README rather than read from the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)`
