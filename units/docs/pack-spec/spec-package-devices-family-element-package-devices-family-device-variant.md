---
id: "spec-package-devices-family-element-package-devices-family-device-variant"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../device/variant"
summary: "Defines a device variant. The element is optional. Can exist multiple times."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Defines a device variant. The element is optional. Can exist multiple times.

**Example**
```
<device Dname="STM32F205RB">
  ...
  <variant Dvariant="STM32F205RBT6">
    <book name="doc\STM32F2_RM.PDF" title="STM32F2 Reference Manual"/>
    <description>Use this device as an alternative.</description>
    <feature type="QFP" count="64" name="LQFP 64 10x10x1.4" />
    <feature type="Temp" n="-40" m="85" name="Industrial Temperature Range"/>
  </variant>
  <variant Dvariant="STM32F205RBT7">
    <feature type="QFP" count="64" name="LQFP 64 10x10x1.4" />
    <feature type="Temp" n="-40" m="105" name="Extended Temperature Range"/>
  </variant>
  ...
</device>
```

\n



  | 
    Parents | 
    Element Chain | 
  

  | 
    device | 
    element_device | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Dvariant | 
    **May get replaced by 'Dname' in the future**. Name of the device on the variant level. This effectively 
        overwrites the device name specified on the device level. 
        Once a device section contains a variant section, only the variant elements describe a 'selectable' device
        which can be selected in the tools. The Dname of the device level effectively becomes a group name like the
        Dfamily and DsubFamily attributes. Only alphabetical characters, decimal digits, '-' and '_' are allowed | 
    RestrictedStringDname | 
    required | 
  

  | 
    Dname | 
    **future**. Name of the device on the variant level. Only alphabetical characters, decimal digits, '-' and '_' are allowed | 
    RestrictedStringDname | 
    required | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    processor | 
    Specify processors that are specific to this device. | 
    ProcessorType | 
    0..* | 
  

  | 
    debugconfig | 
    Specify default settings for the debug connection specific to this device. | 
    DebugConfigType | 
    0..1 | 
  

  | 
    compile | 
    Specify compile or translate options specific to this device. | 
    CompileType | 
    0..* | 
  

  | 
    memory | 
    Specify memory areas that specific to this device. | 
    MemoryType | 
    0..* | 
  

  | 
    algorithm | 
    Specify Flash programming algorithms that can be used by this device. | 
    AlgorithmType | 
    0..* | 
  

  | 
    book | 
    Specify documents specific to this device. | 
    BookType | 
    0..* | 
  

  | 
    description | 
    Description specific to this device. | 
    DescriptionType | 
    0..* | 
  

  | 
    feature | 
    Specify the features of this device. | 
    DeviceFeatureType | 
    0..* | 
  

  | 
    environment | 
    Specify tool options. | 
    EnvironmentType | 
    0..* | 
  

  | 
    debugport | 
    Describe a debug port specific to this device. | 
    DebugPortType | 
    0..* | 
  

  | 
    accessportV1 | 
    Describe an access port (APv1) specific to this device. | 
    AccessPortV1Type | 
    0..* | 
  

  | 
    accessportV2 | 
    Describe an access port (APv2) specific to this device. | 
    AccessPortV2Type | 
    0..* | 
  

  | 
    debug | 
    Specify debug options specific to this device. | 
    DebugType | 
    0..* | 
  

  | 
    trace | 
    Specify trace options specific to this device. | 
    TraceType | 
    0..* | 
  

  | 
    debugvars | 
    Define debug access variables for user-defined settings specific to this device. | 
    DebugVarsType | 
    0..1 | 
  

  | 
    sequences | 
    Describe debug access sequences specific to this device. | 
    SequencesType | 
    0..1 | 
  



\delim
