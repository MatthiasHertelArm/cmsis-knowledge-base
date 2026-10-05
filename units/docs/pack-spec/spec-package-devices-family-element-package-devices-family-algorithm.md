---
id: "spec-package-devices-family-element-package-devices-family-algorithm"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../algorithm"
summary: "Specify Flash programming algorithms with the address range and its size. An algorithm with \\<default> set to true gets configured automatically to the download options of the project. Algorithms can be defined on various levels."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify Flash programming algorithms with the address range and its size.  An algorithm with
\`<default>` set to `true` gets configured automatically to the download options of the project.
Algorithms can be defined on various levels. If the memory range and style are identical, the one
on the lower level takes precedence.

Multiple \`<algorithm>` elements are possible. But as they are uniquely identified by their names, all
algorithms must have a different name.

**Example**
```
<family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
  ...
  <!-- use for all devices of the family  -->
  <algorithm name="Flash\STM32F2xx_512.flm" start=0x08000000 size=0x10000 default="1" style="Keil"/>
 
  <subFamily DsubFamily="STM32F405">
    <!-- use for all devices of a subFamily -->
    <algorithm name="Flash/STM32F2xx_1024.flm" start=0x08000000 size=0x20000 default="1" style="Keil"/>       

    <device Dname="STM32F405OE">
      <!-- finally, this is the default for the device -->
      <algorithm name="Flash/STM32F2xx_2048.flm" start=0x08000000 size=0x40000 default="1" style="Keil"/>
    </device>
    ...
</family>
```


 		



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Attributes | Description | Type | Use |
| Pname | Processor identifier. This attribute **is mandatory for devices that embed multiple processors that require different algorithms**. Only alphabetical characters, decimal digits, '-' and '_' are allowed. | RestrictedString | optional |
| name | Flash Programming Algorithm file including the path, which is relative to the root folder of the software pack. | xs:string | required |
| start | Base address for the Flash programming algorithm. | NonNegativeInteger | required |
| size | Size covered by the Flash programming algorithm. End address = start + size - 1 | NonNegativeInteger | required |
| RAMstart | Base address for the RAM where the Flash programming algorithm will be executed from. If specified, the memory element does not require a `default` attribute. If not specified, a memory element must be defined with the "rwx" access permission and default="1". | NonNegativeInteger | optional |
| RAMsize | Maximum size of RAM available for the execution of the Flash programming algorithm. End address = start + size - 1 is used for the Stack. If specified, the element_memory "memory" element does not require a `default` attribute. If not specified, a memory element must be defined with the "rwx" access permission and default="1". | NonNegativeInteger | optional |
| default | If `true`, then this is the default Flash programming algorithm that gets configured in a project. If not specified or set to `false`, then the Flash programming algorithm can be configured on a lower level. However, the Flash programming algorithm of a project can be changed manually at any time during development. | xs:boolean | optional |
| style | [Version 1.4.0] Today, different toolchains support different styles of incompatible flash programming algorithms. The attribute specifies the style of the specified flash programming algorithm. For backward compatibility the default value is `Keil`. The aim is to converge to the CMSIS style. | AlgorithmStyleEnum | optional |




\delim
