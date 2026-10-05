---
id: "svd-device-peripherals-element-device-peripherals-peripheral-interrupt"
type: "concept"
domain: "pack"
title: "/device/peripherals element: /device/peripherals/peripheral/interrupt element"
summary: "A peripheral can have multiple interrupts. This entry allows the debugger to show interrupt names instead of interrupt numbers."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html"
license: "Apache-2.0"
mode: "V"
---

A peripheral can have multiple interrupts. This entry allows the debugger to show interrupt names instead of interrupt numbers.


**/device/peripherals/peripheral/interrupt**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| peripheral | elem_peripheral |  |  |
| Child Elements | Description | Type | Occurrence |
| name | The string represents the interrupt name. | stringType | 1..1 |
| description | The string describes the interrupt. | xs:string | 0..1 |
| value | Represents the enumeration index value associated to the interrupt. | xs:integer | 1..1 |
