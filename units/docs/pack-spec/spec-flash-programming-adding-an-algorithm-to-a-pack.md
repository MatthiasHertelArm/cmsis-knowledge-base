---
id: "spec-flash-programming-adding-an-algorithm-to-a-pack"
type: "concept"
domain: "pack"
title: "Flash Programming: Adding an Algorithm to a Pack"
summary: "The generated .FLM file needs to be added to the DFP, so that it is available to the tool user for programming his device. Usually, a directory Flash is created and the algorithm is saved in this directory."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/flashAlgorithm.html"
license: "Apache-2.0"
mode: "V"
---

The generated ***.FLM** file needs to be added to the DFP, so that it is available to the tool user for programming
his device. Usually, a directory **Flash** is created and the algorithm is saved in this directory.

The algorithm is specified within the the element_family level:
```
<family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
  ...
  <algorithm name="Flash/STM32F2xx_512.flm" start=0x08000000 size=0x10000 default="1"/>         <!-- valid for all devices of the family  -->
 
  <subFamily DsubFamily="STM32F405">
    <algorithm name="Flash/STM32F2xx_1024.flm" start=0x08000000 size=0x20000 default="1"/>       <!-- valid for all devices of a subFamily -->
 
    <device Dname="STM32F405OE">
      <algorithm name="Flash/STM32F2xx_2048.flm" start=0x08000000 size=0x40000 default="1"/>     <!-- finally, this is the default for the device -->
    </device>
    ...
</family>
```

The argument _start_ specifies the base address for the Flash programming algorithm.

The argument _size_ specifies the size covered by the Flash programming algorithm. End address = start + size - 1.

The argument _default_ specifies whether a Flash programming algorithm is set as the default algorithm in a project (when
`true`). If _default_ is not set or false, the Flash programming algorithm can be configured on a lower level.
However, the Flash programming algorithm of a project can be changed manually at any time during development.
