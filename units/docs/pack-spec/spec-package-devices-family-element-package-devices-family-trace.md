---
id: "spec-package-devices-family-element-package-devices-family-trace"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../trace"
summary: "Describes device capabilities and possible configuration settings for capturing trace. A trace element applies to all processor connections."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes device capabilities and possible configuration settings for capturing trace. A **trace**
element applies to all processor connections.

**Example**
```
<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <trace>
    <serialwire/>
    <traceport width="0x0000000B"/> <!-- support for port widths 1, 2, and 4 -->
    <tracebuffer start="0x2000C000" size="0x4000"/>
  </trace>
  ...
</family>
```


 		



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Child Elements | Description | Type | Occurrence |
| serialwire | Describe the serial wire trace output capabilities of the processor. | SerialWireType | 0..* |
| traceport | Describe the parallel trace port output capabilities of the processor. | TracePortType | 0..* |
| tracebuffer | Describe the on-device trace buffer capabilities of the processor. | TraceBufferType | 0..* |
