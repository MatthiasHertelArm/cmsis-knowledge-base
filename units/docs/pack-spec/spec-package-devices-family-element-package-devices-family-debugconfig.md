---
id: "spec-package-devices-family-element-package-devices-family-debugconfig"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debugconfig"
summary: "Default debugger configuration for a target connection."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Default debugger configuration for a target connection.

**Example**
```

<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <debugconfig default="jtag" clock="10000000" swj="1" sdf="Debug/SDF/lpc4300.sdf"/>
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
    default | 
    
      Specifies the default debug protocol to use for target connections. Predefined tokens must be used as
      defined in Table: Debug Protocol Type. Default value is `swd`.
     | 
    DebugProtocolEnum | 
    optional | 
  

  | 
    clock | 
    Specifies the default debug clock setting in Hz for a target connection. Default value is `10000000`. | 
    xs:unsignedInt | 
    optional | 
  

  | 
    swj | 
    
      The device is accessed via a CoreSight SWJ-DP capable of switching between Serial Wire Debug (SWD) and JTAG protocols.
      Default value is `true`.
     | 
    xs:bool | 
    optional | 
  

  | 
    dormant | 
    
      The device is accessed via a CoreSight DP that requires the dormant state to switch debug protocols.
      Default value is `false`.
     | 
    xs:bool | 
    optional | 
  

  | 
    sdf | 
    
      This attribute specifies the filename and path of the system description file (SDF).
      The system description file contains information about CoreSight components, there versions and how they
      are interconnected and hooked to debug and access ports. If not specified an autodetection needs to
      be initiated by the debugger at connection time.
     | 
    xs:string | 
    optional | 
  




 		

 **Table: Debug Protocol Type**

The table lists the values for debug protocol types. The values can be used in 
 - element_debugconfig



  | 
    type= | 
    Description | 
  

  | 
    jtag | 
    
      JTAG debug protocol.
     | 
  

  | 
    swd | 
    
      Arm Serial Wire Debug (SWD) protocol.
     | 
  

  | 
    cjtag | 
    
      CJTAG concurrent jtag debug protocol.
     |
