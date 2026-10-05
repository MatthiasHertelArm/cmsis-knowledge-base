---
id: "ts-packchk-m335"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M335: which shall contain device specific components.   No condition id set "
status: "draft"
tool: "packchk"
severity: "warning"
code: "M335"
symptoms: ["M335", "Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   No condition id set to specify a rule filtering for a device or set of devices."]
symptom_regex: "^Component 'Cclass=.+?, Cgroup=.+?, Cversion=.+?' is member of the Cclass='.+?' which shall contain device specific components\\.   No condition id set to specify a rule filtering for a device or set of devices\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M335`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   No condition id set to specify a rule filtering for a device or set of devices.`

## Cause

A component defined as 'board support' needs a reference to a device. Add a device or correct the component definition. Refer to attribute _Cclass_ of [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) and [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice).

## Fix

_siehe Cause_
