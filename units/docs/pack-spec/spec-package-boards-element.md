---
id: "spec-package-boards-element"
type: "concept"
domain: "pack"
title: "/package/boards element"
summary: "The level <boards> describes a development board that is the subject of a Board Support Pack (BSP)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

The level **`<boards>`** describes a development board that is the subject of a Board Support Pack (BSP).
It contains information about the board vendor and name, a brief description, images to be displayed on web pages, and
different types of documentation. The microcontroller devices that are mounted on the board or that are compatible with the
ones mounted are also specified. A list of features concludes the `<boards>` section.

A development board is described by the following properties:
- description: a brief description of the development board
- book: documentation about the board (user manuals, schematics, etc.)
- mountedDevice: the microcontroller device mounted on the development board.
- compatibleDevice: compatible microcontroller devices. 
- mountedPart: a part (any device other than the MCU) mounted on the development board.
- image: pictures of the board to be displayed on web pages. 
- feature: categorized list of the development board's features and peripherals. 
- debugInterface: describing the debug capabilities. 
- debugProbe: describing the on-board debug probe.
- memory: additional memory provided by the board
- algorithm: additional flash programming algorithms for the board-specific memory
- environment:  tool specific settings



**Example**
```
  <boards>
    <board vendor="STMicroelectronics" name="32F429IDISCOVERY" revision="Rev.1" salesContact="http://www.st.com/stonline/contactus/contacts/index.php" orderForm="https://my.st.com/esample/app?page=basket&amp;pn=STM32F429I-DISCO">
	 
      <description>STMicroelectronics STM32F429I Discovery Board Support and Examples</description>
	   
      <image small="Images/stm32f429i-disco_small.png" large="Images/stm32f429i-disco.png"/>
	   
      <book category="overview"  name="http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1199/PF259090" title="32F429IDISCOVERY Web Page"/>
      <book category="setup"     name="Documents/UM1662.pdf" title="Getting Started"/>
      <book category="schematic" name="Documents/UM1670.pdf" title="Schematics"/>
      <book category="manual"    name="Documents/UM1670.pdf" title="User Manual"/>
	   
      <mountedDevice    Dvendor="STMicroelectronics:13" Dname="STM32F429ZITx"/>
	   
      <compatibleDevice Dvendor="STMicroelectronics:13" Dfamily="STM32F4 Series" DsubFamily="STM32F429"/>

      <mountedPart n="1" Hvendor="STMicroelectronics" Hname="I3G4250D" Hvariant="I3G4250D"/>
	   
      <feature type="ODbg"      n="1"              name="On-board ST-LINK/V2 with selection mode switch to use the kit as a standalone"/>
      <feature type="XTAL"      n="80000000"/>
      <feature type="PWR"       n="5"              name="USB Powered"/>
      <feature type="PWR"       n="3"  m="5"       name="External Supply"/>
      <feature type="RAM"       n="1"              name="64 MBit SDRAM"/>
      <feature type="DIO"       n="4"  m="32"      name="Extension header for LQFP144 with 2.54 mm Pitch"/>
      <feature type="USB"       n="1"              name="High-Speed USB OTG with micro-AB Connector"/>
      <feature type="ConnOther" n="1"              name="JP3 (Idd) for current measurement"/>
      <feature type="Button"    n="2"              name="Push-buttons: User and Reset"/>
      <feature type="Gyro"      n="1"              name="L3GD20, ST MEMS motion sensor, 3-axis digital output gyroscope"/>
      <feature type="LED"       n="6"              name="Com, 3.3 V Power, Two user, Two USB OTG LEDs"/>
      <feature type="CustomFF"  n="66" m="119.3"   name="Discovery Board Formfactor"/>
      <feature type="GLCD"      n="1"  m="240.320" name="2.4 inch QVGA TFT LCD"/>
	   
      <debugInterface adapter="ST-Link" connector="Mini-USB"/>
      <debugProbe connector="Mini-USB" debugClock="10000000" debugLink="swd" name="ST-Link"/>   
    </board>
  </boards>
```
