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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Define the device [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) or correct the information about the device in the reference."
summary: "A component whose Cclass is one that must hold device-specific components (such as Device or Startup) references a condition that contains no rule filtering for a device or set of devices. packchk therefore cannot tell which devices the component …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M336`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%, condition=%COND%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   The referenced condition id does not contain a rule filtering for a device or set of devices.`

## Cause

A component whose Cclass is one that must hold device-specific components (such as Device or Startup) references a condition that contains no rule filtering for a device or set of devices. packchk therefore cannot tell which devices the component applies to. The variable parts name the component's Cclass, Cgroup, Cversion and the condition id taken from the PDSC.

## Fix

Make the condition filter on a device or device family, so the referenced condition includes a Device or Device family rule (for example a require element for Dname or Dfamily), or move the component to a condition that already does so. Also check that the <device> definition in the PDSC matches the device the condition refers to.

## Note

Only the message text and README cause were available; the source lines around the trigger could not be checked, so the mechanism is inferred from the message and README. The README fix (define the device or correct the device reference) is consistent with this reading.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
