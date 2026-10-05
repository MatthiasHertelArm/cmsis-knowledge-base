---
id: "ts-packchk-m336"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M336: Component 'Cclass=…, Cgroup=…, Cversion=…, condition=…' is member of the Cclass='…' which shall …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M336"
symptoms: ["M336", "Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%, condition=%COND%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   The referenced condition id does not contain a rule filtering for a device or set of devices."]
symptom_regex: "^Component 'Cclass=.+?, Cgroup=.+?, Cversion=.+?, condition=.+?' is member of the Cclass='.+?' which shall contain device specific components\\.   The referenced condition id does not contain a rule filtering for a device or set of devices\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Define the device [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) or correct the information about the device in the reference."
summary: "A component with Cclass \"Device\", \"Board Support\", or \"CMSIS Driver\" without Csub has a condition, but neither that condition nor the conditions it references contains an expression whose Dname matches a device known to packchk (this pack or PDSC …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:153-154", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckComponents.cpp:104-110", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckComponents.cpp:155-207", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:177"]
---

## Symptom

`M336`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%, condition=%COND%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   The referenced condition id does not contain a rule filtering for a device or set of devices.`

## Cause

A component with Cclass "Device", "Board Support", or "CMSIS Driver" without Csub has a condition, but neither that condition nor the conditions it references contains an expression whose Dname matches a device known to packchk (this pack or PDSC files passed with -i).

## Fix

Add <require Dvendor="..." Dname="..."/> for the supported devices to the component's condition and make sure those devices exist in this pack or in a PDSC passed with -i; M364 lines name Dname values that matched no device.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:153-154`
- `tools/packchk/src/CheckComponents.cpp:104-110`
- `tools/packchk/src/CheckComponents.cpp:155-207`
- `tools/packchk/README.md:177`
