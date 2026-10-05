---
id: "spec-package-devices-family-element-package-devices-family-device"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/../device"
summary: "Define properties that are specific to a device. Properties defined on upper levels get inherited, unless they can be overwritten. Multiple \\<device> elements can be defined."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Define properties that are specific to a device. Properties defined on upper levels get inherited, unless they can be overwritten.
Multiple \`<device>` elements can be defined.

**Example**
```
<subFamily DsubFamily="STM32F405">
  ...
  <device Dname="STM32F405OE">
    <memory    name="Flash" access="rx" start="0x08000000" size="0x80000" startup="1" default="1"/>
    <algorithm name="Flash/STM32F4xx_1024.flm" start="0x08000000" size="0x80000" default="1" style="Keil"/>
    <feature   type="IOs" n="72" name="Input and Output Ports"/>
  </device>

  <device Dname="STM32F405OG">
    <memory    name="Flash" access="rx" start="0x08000000" size="0x100000" startup="1" default="1"/>
    <algorithm name="Flash/STM32F4xx_1024.flm" start="0x08000000" size="0x100000" default="1" style="Keil"/>
    <feature   type="IOs" n="72" name="Input and Output Ports"/>
  </device>
  ...
</subFamily>
```


 



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| Attributes | Description | Type | Use |
| Dname | Specifies the name of the device. Only alphabetical characters, decimal digits, '-' and '_' are allowed. | RestrictedString | required |
| Child Elements | Description | Type | Occurrence |
| processor | Specify processors that are specific to this device. | ProcessorType | 0..* |
| debugconfig | Specify default settings for the debug connection specific to this device. | DebugConfigType | 0..1 |
| compile | Specify compile or translate options specific to this device. | CompileType | 0..* |
| memory | Specify memory areas that specific to this device. | MemoryType | 0..* |
| algorithm | Specify Flash programming algorithms that can be used by this device. | AlgorithmType | 0..* |
| flashinfo | Specify additional information required to download application code into Flash that is specific to this device. | FlashInfoType | 0..* |
| book | Specify documents specific to this device. | BookType | 0..* |
| description | Description specific to this device. | DescriptionType | 0..* |
| feature | Specify the features of this device. | DeviceFeatureType | 0..* |
| environment | Specify tool options. | EnvironmentType | 0..* |
| debugport | Describe a debug port specific to this device. | DebugPortType | 0..* |
| accessportV1 | Describe an access port (APv1) specific to this device. | AccessPortV1Type | 0..* |
| accessportV2 | Describe an access port (APv2) specific to this device. | AccessPortV2Type | 0..* |
| debug | Specify debug options specific to this device. | DebugType | 0..* |
| trace | Specify trace options specific to this device. | TraceType | 0..* |
| debugvars | Define debug access variables for user-defined settings specific to this device. | DebugVarsType | 0..1 |
| sequences | Describe debug access sequences specific to this device. | SequencesType | 0..1 |
| variant | Complex element specifying a variant of a device. | xs:ComplexType | 0..* |



\delim
