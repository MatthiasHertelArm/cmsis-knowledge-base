---
id: "spec-package-devices-family-element-package-devices-family-debugport-jtag"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debugport/jtag"
summary: "Indicates availability of a JTAG interface for the debugport parent element. Its attributes allow the manual override of a debugger's automatic JTAG Test Access Port (TAP) detection."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Indicates availability of a JTAG interface for the **debugport** parent element. Its
attributes allow the manual override of a debugger's automatic JTAG Test Access Port (TAP)
detection.

**Example**
```
<family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
  ...
  <debugconfig default="swd" clock="10000000" swj="1"/>
  
  <debugport __dp="0">
    <jtag tapindex="0" idcode="0x4BA00477" irlen="4"/>
    <swd  idcode="0x2BA01477"/>
  </debugport>
  ...
</family>
```


 		



  | 
    Parents | 
    Element Chain | 
  

  | 
    debugport | 
    element_debugport | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    tapindex | 
    Specifies the TAP index relative to the JTAG scan chain of this device. A debugger needs to determine the absolute index
    if the device is part of an extended scan chain. Default value is `0`.  | 
    NonNegativeInteger | 
    optional | 
  

  | 
    idcode | 
    Specifies the IDCODE of the JTAG TAP. This value overrides the IDCODE read from the target.  | 
    NonNegativeInteger | 
    optional | 
  

<!-- finalize when there are multidrop devices available (or when we have DS-5 support for that)
  | 
    targetsel | 
    Specifies the value to write to a CoreSight debug port's TARGETSEL register to select this port for connection.
    The element is required for debug ports with multi-drop support. It is ignored otherwise. **(Unsupported)** | 
    NonNegativeInteger | 
    optional | 
  

-->
  | 
    irlen | 
    Specifies the instruction register length of the JTAG TAP. This value overrides the instruction register length detected by a debugger.  | 
    xs:unsignedInt | 
    optional |
