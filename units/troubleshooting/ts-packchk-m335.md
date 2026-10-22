---
id: "ts-packchk-m335"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M335: Component 'Cclass=…, Cgroup=…, Cversion=…' is member of the Cclass='…' which shall contain device …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M335"
symptoms: ["M335", "Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   No condition id set to specify a rule filtering for a device or set of devices."]
symptom_regex: "^Component 'Cclass=.+?, Cgroup=.+?, Cversion=.+?' is member of the Cclass='.+?' which shall contain device specific components\\.   No condition id set to specify a rule filtering for a device or set of devices\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "A component defined as 'board support' needs a reference to a device. Add a device or correct the component definition. Refer to attribute _Cclass_ of [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) and [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice)."
summary: "packchk prints M335 when a component whose Cclass is the device-specific class (such as 'Device' or 'Board Support' as named in the spec) carries no condition id that filters it to a device or device set."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M335`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   No condition id set to specify a rule filtering for a device or set of devices.`

## Cause

packchk prints M335 when a component whose Cclass is the device-specific class (such as 'Device' or 'Board Support' as named in the spec) carries no condition id that filters it to a device or device set. The component therefore cannot be tied to a device, which the PDSC spec requires for that class. The README attributes this to a 'board support' component missing a device reference.

## Fix

Give the component a condition that references the target device or device family, or correct the component's Cclass/Cgroup so it is not a device-specific class. Check the component's Cclass attribute against the PDSC component element documentation, and add a mountedDevice reference if it is a board support component.

## Note

Only the message text and README were available; the source trigger lines could not be inspected, so the condition check and exact wording are inferred. The README cause and the message text disagree slightly on whether the class is 'board support' or a generic device-specific class; the fix should be verified against the actual check in packchk.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
