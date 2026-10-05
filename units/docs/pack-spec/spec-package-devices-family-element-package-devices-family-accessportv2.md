---
id: "spec-package-devices-family-element-package-devices-family-accessportv2"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../accessportV2"
summary: "Describes a CoreSight access port (APv2) of the device as introduced with the Arm Debug Interfaces (ADI) v6 and its selection parameters. The element can occur on various levels."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a CoreSight access port (APv2) of the device as introduced with the Arm Debug Interfaces (ADI) v6 and its selection parameters.
The element can occur on various levels. Use unique ID values for the attribute **__apid** to distinguish multiple **accessportV1** and **accessportV2** elements in later references.

An **accessportV2** must be later selected via **__apid**. It is not possible to use a pair of **__dp** and **__ap** values.


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
  <accessportV1 __apid="0" _dp="0" index="0"/>
  <accessportV1 __apid="1" _dp="0" index="1"/>
    
  <!-- ADIv6 DAP -->
  <accessportV2 __apid="2" _dp="1" address="0x00002000"/>
  <accessportV2 __apid="3" _dp="1" address="0x00004000"/>
    
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
    address | 
    
      The address to select this access port in its parent's address space for a target access.
     | 
    NonNegativeInteger | 
    required | 
  

  | 
    HPROT | 
    
      Value for HPROT (AHB Protection Control) bits.
     | 
    NonNegativeInteger | 
    optional | 
  

  | 
    SPROT | 
    
      Value for SPROT (Secure Protection Control) bit.
     | 
    NonNegativeInteger | 
    optional | 
  

  | 
    parent | 
    
      Reference to the **__apid** of the parent access port if the system contains nested APv2 access ports.

      **parent** must not be specified if the access port is directly connected to the **debugport**.
     | 
    xs:unsignedInt | 
    optional |
