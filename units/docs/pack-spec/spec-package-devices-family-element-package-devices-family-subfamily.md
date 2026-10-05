---
id: "spec-package-devices-family-element-package-devices-family-subfamily"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/subFamily"
summary: "Define properties that are in common to all devices of a subFamily. This is another mechanism of granulation to reduce redundancy. These properties are inherited by subgroups or elements. Multiple \\<subFamily> groups can be defined."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Define properties that are in common to all devices of a subFamily. This is another mechanism of granulation to reduce redundancy. 
These properties are inherited by subgroups or elements. Multiple \`<subFamily>` groups can be defined.
 
**Example**
```
<family Dfamily="STM32F2" Dvendor="STMicroelectronics:13">
  ...   
  <subFamily DsubFamily="...">
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
    <device Dname="...">
      ...
    </device>
  </subFamily>

  <subFamily DsubFamily="STM32F2xx">
    ...
  </subFamily>

</family>
```


 



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| Attributes | Description | Type | Use |
| DsubFamily | Name of the device sub family. | xs:string | required |
| Child Elements | Description | Type | Occurrence |
| processor | Specify processors that are available in all devices of the sub-family. | ProcessorType | 0..* |
| compile | Specify compile or translate options that are relevant to all devices of the sub-family. | CompileType | 0..* |
| debugconfig | Specify default settings for the debug connection relevant to all devices of the sub-family. | DebugConfigType | 0..1 |
| debugvars | Define global debug access variables for user-defined settings relevant to all devices of the sub-family. | DebugVarsType | 0..1 |
| sequences | Describe debug access sequences relevant to all devices of the sub-family. | SequencesType | 0..1 |
| debugport | Describe a debug port relevant to all devices of the sub-family. | DebugPortType | 0..* |
| accessportV1 | Describe an access port (APv1) relevant to all devices of the sub-family. | AccessPortV1Type | 0..* |
| accessportV2 | Describe an access port (APv2) relevant to all devices of the sub-family. | AccessPortV2Type | 0..* |
| debug | Specify debug options that are relevant to all devices of the sub-family. | DebugType | 0..* |
| trace | Specify trace options that are relevant to all devices of the sub-family. | TraceType | 0..* |
| memory | Specify memory areas that are available in all device of the sub-family. | MemoryType | 0..* |
| algorithm | Specify Flash programming algorithms that can be used by all device of the sub-family. | AlgorithmType | 0..* |
| flashinfo | Specify additional information required to download application code into Flash that is available for all devices of the sub-family. | FlashInfoType | 0..* |
| book | Specify documents relevant for all device of the sub-family. | BookType | 0..* |
| description | Description of the device family. | DescriptionType | 0..* |
| environment | Specify tool specific settings. | EnvironmentType | 0..* |
| feature | Specify features available in devices of the sub-family. | DeviceFeatureType | 0..* |
| device | List individual devices that belong to the device sub-family. | DeviceType | 0..* |
