---
id: "spec-package-devices-family-element-package-devices-family"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family"
summary: "Define properties that are in common to all devices of a family. These properties are inherited by subgroups or elements. This is a mechanism of granulation to reduce redundancy. Multiple \\<family> groups can be defined."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Define properties that are in common to all devices of a family. These properties are inherited by 
subgroups or elements. This is a mechanism of granulation to reduce redundancy.  
Multiple \`<family>` groups can be defined.
 
**Example**
```
<devices>
  ...
  <family Dfamily="STM32F2" Dvendor="STMicroelectronics:13">
    <processor   .../>
    <debugconfig .../>
    <debugvars   .../>
    <sequences   .../>
    <compile     .../>
    <memory      .../>
    <algorithm   .../>
    <book        .../>
    <description> Write texte here </description>
    <environment> ... </environment>
    <feature     .../>
    <debugport   .../>
    <debug       .../>
    <trace       .../>
   
    <subFamily DsubFamily="...">
      ...
      <device Dname="...">
        ...
      </device>
      ...
    </subFamily>
    ...
  </family>
  ...
</devices>
```


 



  | 
    Parents | 
    Element Chain | 
  

  | 
    devices | 
    element_devices | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Dfamily | 
    Name of the device family. | 
    xs:string | 
    required | 
  

  | 
    Dvendor | 
    Device vendor name.  Use predefined values as listed in the table Device Vendor. | 
    DeviceVendorEnum | 
    required | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    processor | 
    List all processors that are in common to devices of the family. | 
    ProcessorType | 
    0..* | 
  

  | 
    debugconfig | 
    Specify default settings for the debug connection relevant to all devices of the family. | 
    DebugConfigType | 
    0..1 | 
  

  | 
    compile | 
    Specify compile or translate options that are relevant to all devices of the family. | 
    CompileType | 
    0..* | 
  

  | 
    debugvars | 
    Define global debug access variables for settings relevant to all devices of the family unless replaced by debugvars on subFamily, device or variant level | 
    DebugVarsType | 
    0..1 | 
  

  | 
    sequences | 
    Describe debug access sequences relevant to all devices of the family. | 
    SequencesType | 
    0..1 | 
  

  | 
    debugport | 
    Describe a debug port relevant to all devices of the family. | 
    DebugPortType | 
    0..* | 
  

  | 
    accessportV1 | 
    Describe an access port (APv1) relevant to all devices of the family. | 
    AccessPortV1Type | 
    0..* | 
  

  | 
    accessportV2 | 
    Describe an access port (APv2) relevant to all devices of the family. | 
    AccessPortV2Type | 
    0..* | 
  

  | 
    debug | 
    Specify debug options that are relevant to all devices of the family. | 
    DebugType | 
    0..* | 
  

  | 
    trace | 
    Specify trace options that are relevant to all devices of the family. | 
    TraceType | 
    0..* | 
  

  | 
    memory | 
    Specify memory areas that are available for all devices of the family. | 
    MemoryType | 
    0..* | 
  

  | 
    algorithm | 
    Specify Flash programming algorithms that are suitable for all devices. | 
    AlgorithmType | 
    0..* | 
  

  | 
    flashinfo | 
    Specify additional information required to download application code into Flash that is available for all devices of the family. | 
    FlashInfoType | 
    0..* | 
  

  | 
    book | 
    Specify documents that are relevant for all devices of a family. | 
    BookType | 
    0..* | 
  

  | 
    description | 
    Describe the device family. | 
    DescriptionType | 
    0..* | 
  

  | 
    environment | 
    Specify tool specific settings. | 
    EnvironmentType | 
    0..* | 
  

  | 
    feature | 
    Specify features that are available in all members of the device family. | 
    DeviceFeatureType | 
    0..* | 
  

  | 
    subFamily | 
    A optional sub-family that is used to group devices. | 
    group | 
    0..* | 
  

  | 
    device | 
    Individual devices that belong to the device family. | 
    DeviceType | 
    0..* |
