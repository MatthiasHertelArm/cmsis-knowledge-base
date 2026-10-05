---
id: "spec-package-devices-family-element-package-devices-family-accessportv1"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../accessportV1"
summary: "Describes a CoreSight access port (APv1) of the device and its selection parameters. The element can occur on various levels. Use unique ID values for the attribute apid to distinguish multiple accessportV1 and accessportV2 elements in later references."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a CoreSight access port (APv1) of the device and its selection parameters. The element can occur on various
levels. Use unique ID values for the attribute **__apid** to distinguish multiple **accessportV1** and **accessportV2**
elements in later references.

**accessportV1** elements are required for targets that mix ADIv5 and ADIv6 debug ports and hence also have APv2 access ports.
Pairs of **__dp** and **__ap** values must not be used to reference an access port if a debug description describes access port elements.


**Example**
```

<family Dvendor="ARM:82" Dfamily="...">
  ...
  <debugport __dp="0">  <!-- ADIv5 DAP -->
    <jtag tapindex="0"/>
    <swd/>
  </debugport>
  
  <debugport __dp="1">  <!-- ADIv6 DAP -->
    <jtag tapindex="1"/>
  </debugport>

  <!-- ADIv5 DAP -->
  <accessportV1 __apid="0" __dp="0" index="0"/>
  <accessportV1 __apid="1" __dp="0" index="1"/>
    
  <!-- ADIv6 DAP -->
  <accessportV2 __apid="2" __dp="1" address="0x00002000"/>
  <accessportV2 __apid="3" __dp="1" address="0x00004000"/>
   
  ...
</family>
```


 		



  | 
    Parents | 
    Element Chain | 
  

  | 
    family | 
    element_family | 
  

  | 
    subFamily | 
    element_subFamily | 
  

  | 
    device | 
    element_device | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    __apid | 
    
      Unique ID of this element with respect to other access port elements.
      It must be used consistently in references within the scope of the parent section.
     | 
    xs:unsignedInt | 
    required | 
  

  | 
    __dp | 
    
      Unique ID of the **debugport** used to access this access port.
      Optional if exactly one **debugport** exists.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    index | 
    
      The index to select this access port for a target access.
     | 
    xs:unsignedInt | 
    required |
