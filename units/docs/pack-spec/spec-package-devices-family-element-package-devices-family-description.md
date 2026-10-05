---
id: "spec-package-devices-family-element-package-devices-family-description"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../description"
summary: "Brief description of the element. Can occur on various levels and gets inherited from upper level if not defined in the element. Should only contain the unique features of the element. Number of bullet points should not exceed ten."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Brief description of the element. Can occur on various levels and gets inherited from upper level if not defined in the element. Should only contain the unique features of the element. Number
of bullet points should not exceed ten. To create a detailed feature list use the element_feature instead.

**Example**
```
<package>
  <devices>
    <family Dfamily="STM32F2" Dvendor="STMicroelectronics:13">
    
      <description>
        STM32F2 devices are designed for medical, industrial and consumer
        applications and provide rich connectivity peripherals.
        - At 120 MHz CPU clock: 150 DMIPS executing from Flash memory 
        - ART Accelerator for low-power Flash execution (175 µA/MHz @ 120 MHz)
        - Flexible Memory Controller supports Compact Flash, SRAM, PSRAM, NOR and NAND
      </description>
 
    </family>
  </devices>
</package>
```


 



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Attributes | Description | Type | Use |
| Pname | Processor Identifier. This attribute **is mandatory for devices that embed multiple processors and where the description is specific to a single processor**. Only alphabetical characters, decimal digits, '-' and '_' are allowed. | RestrictedString | optional |
