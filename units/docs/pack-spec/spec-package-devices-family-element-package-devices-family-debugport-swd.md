---
id: "spec-package-devices-family-element-package-devices-family-debugport-swd"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debugport/swd"
summary: "Indicates availability of an Arm Serial Wire Debug (SWD) interface for the debugport parent element."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Indicates availability of an Arm Serial Wire Debug (SWD) interface for the **debugport** parent element.
Its attributes allow the manual override of SWD port characteristics as read from the target and provide
information for the port selection in a system with multi-drop SWD support.

**Example**
```
<family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
  ...
  <debugconfig default="swd" clock="10000000" swj="1"/>
  
  <debugport __dp="0">
    <jtag tapindex="0" idcode="0x4BA00477" irlen="4"/>
    <swd idcode="0x2BA01477"/>
  </debugport>
  ...
</family>
```


 		



| Parents | Element Chain |  |  |
|---|---|---|---|
| debugport | element_debugport |  |  |
| Attributes | Description | Type | Use |
| idcode | Specifies the IDCODE of the SWD port. It overrides the value read from the port's IDCODE register. | NonNegativeInteger | optional |
| targetsel | Specifies the value to write to a CoreSight debug port's TARGETSEL register to select this port for connection. The element is required for debug ports with multi-drop SWD support. It is ignored otherwise. **(Unsupported)** | NonNegativeInteger | optional |
