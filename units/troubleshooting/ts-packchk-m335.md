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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "A component defined as 'board support' needs a reference to a device. Add a device or correct the component definition. Refer to attribute _Cclass_ of [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) and [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice)."
summary: "A component with Cclass \"Device\", \"Board Support\", or \"CMSIS Driver\" without Csub has no condition attribute, so nothing restricts it to the devices it supports."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:151-152", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckComponents.cpp:84-107", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:176"]
---

## Symptom

`M335`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   No condition id set to specify a rule filtering for a device or set of devices.`

## Cause

A component with Cclass "Device", "Board Support", or "CMSIS Driver" without Csub has no condition attribute, so nothing restricts it to the devices it supports.

## Fix

Add a condition that requires the supported devices and reference it from the component, e.g. <condition id="ARMCM4"><require Dvendor="ARM:82" Dname="ARMCM4*"/></condition> and <component Cclass="Device" Cgroup="Startup" ... condition="ARMCM4">.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:151-152`
- `tools/packchk/src/CheckComponents.cpp:84-107`
- `tools/packchk/README.md:176`
