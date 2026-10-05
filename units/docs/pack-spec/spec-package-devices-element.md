---
id: "spec-package-devices-element"
type: "concept"
domain: "pack"
title: "/package/devices element"
summary: "The level \\elem{devices} contains all devices for which support is provided by the software pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_devices_pg.html"
license: "Apache-2.0"
mode: "V"
---

The level \elem{devices} contains all devices for which support is provided by the software pack. 

Devices can be organized in hierarchy groups to limit redundancy. The hierarchy levels are:
- family: the attributes of a device family which includes also the processor.
- subFamily: attributes of an optional sub-family; this adds or modifies features of a family.

Device characteristics can be defined in:
- device: attributes of a specific silicon device
- variant: attributes of a device variant (for example, with different package or temperature range) or an 
       OEM device or board that integrates the device.
       
A device is described by the following properties:
 - description: textual device description
 - feature: categorized list of device peripherals and features
 - book: documentation about the device and its processor(s)
 - processor: processor and processor features embedded in the device
 - compile: device specific general settings for the build tools
 - debugconfig: default settings for a debug connection
 - debugvars: global debug access variables for use in sequences.
 - sequences: debug access sequences.
 - debugport: debug port description of the device for the debugger to configure a debug connection.
 - accessportV1: access port (APv1) description of the device for the debugger to configure a debug connection.
 - accessportV2: access port (APv2) description of the device for the debugger to configure a debug connection.
 - debug: device specific information for the debugger to configure a debug connection including System View Description files.
 - trace: device specific information for the debugger to configure trace.
 - memory: memory layout of the device for internal and external RAM and ROM regions
 - algorithm: device specific Flash programming algorithms

A device will inherit the specifications from both the family and sub-family levels. Some properties are required to be unique. 
For example, the name of the svd file attribute of the \elem{debug} property. 
Therefore, the svd file specified on the family level can be redefined by the attribute on the sub-family or device level.
Information like the description and feature entries are concatenated, starting with the information from the family and sub-family level
and finalizing with the information on the device level.

**Example**
```
<package>
  ...
  <devices>
    <!-- family level -->
    <family Dfamily="STM32F2" Dvendor="STMicroelectronics:13">
      <processor Dcore="Cortex-M3" DcoreVersion="r2p1"
                 Dfpu="NO_FPU" Dmpu="MPU" Dendian="Little-endian" Dclock="120000000"/>

      <compile   header="Device/Include/stm32f2xx.h" define="STM32F2XX"/>
      <debug     svd="SVD/STM32F20x.svd"/>
      <algorithm name="Flash/STM32F2xx_OPT.flm" start="0x1FFFC000" size="0x00000010" style="Keil"/>
      <book      name="doc/STM32F2.PDF" title="STM32F2 Reference Manual"/>

      <description>
        Arm 32-bit Cortex-M3 CPU based Microcontroller
        - 120 MHz maximum frequency producing 150 DMIPS/1.25 DMIPS/MHz
        - Memory Protection Unit
        - Flexible static memory controller (supports Compact Flash, SRAM, PSRAM, NOR, NAND memories)
        - LCD parallel interface, 8080/6800 modes
        - Clock, reset and supply management
      </description>

      <feature type="Timer" n="10" m="32" name="General Purpose Timer with 60 MHz"/>
      <feature type="Timer" n="2" m="16" name="Advanced Control Timer with 120 MHz"/>
      <feature type="Timer" n="2" m="16" name="Basic Timer with 60 MHz"/>
      <feature type="TimerOther" n="1" name="Independent Watchdog Timer"/>
      <feature type="TimerOther" n="1" name="Window Watchdog Timer"/>
      <feature type="DAC" n="2" m="12"/>
      <feature type="SPI" n="3" name="SPI Interface (two of them can be used as I2S)"/>
      <feature type="I2C" n="3"/>
      <feature type="USART" n="4" name="USART Interface up to 7.5 Mbit/s"/>
      <feature type="UART" n="2" name="UART Interface up to 3.75 Mbit/s"/>
      <feature type="USBOTG" n="1"  name="USB OTG (Full-Speed) with PHY and ULPI"/>
      <feature type="USBOTG" n="1"  name="USB OTG (High-Speed) with PHY and ULPI"/>
      <feature type="CAN" n="2"  name="CAN Interface (2.0b Active)"/>
      <feature type="SDIO" n="1" m="8" name="Supporting SD/MicroSD/MMC"/>
      <feature type="VCC" n="1.8" m="3.6"/>
      <feature type="NPU" n="Ethos-U55"/>

      <!-- sub family level -->
      <subFamily DsubFamily="128 Flash">
        <memory name="SRAM"  access="rwx" start="0x20000000" size="0x10000" default="1"/>
        <memory name="Flash" access="rx"  start="0x08000000" size="0x20000" startup="1" default="1"/>

        <!-- device level -->
        <device Dname="STM32F205RB">
          <feature type="IOs" n="51" name="Input and Output Ports"/>
          <variant Dvariant="STM32F205RBT6">
            <feature type="QFP" count="64" name="LQFP 64 10x10x1.4" />
            <feature type="Temp" n="-40" m="85" name="Industrial Temperature Range"/>
          </variant>
          <variant Dvariant="STM32F205RBT7">
            <feature type="QFP" count="64" name="LQFP 64 10x10x1.4" />
            <feature type="Temp" n="-40" m="105" name="Extended Temperature Range"/>
          </variant>
        </device>

        <device Dname="STM32F205VB">
          <feature type="IOs" n="82" name="Input and Output Ports"/>
          <variant Dvariant="STM32F205VBT6">
            <feature type="QFP" count="100" name="LQFP 100 14x14x1.4" />
            <feature type="Temp" n="-40" m="85" name="Industrial Temperature Range"/>
          </variant>
        </device>
      </subFamily>

    </family>
  </devices>
</package>
```
