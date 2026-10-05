---
id: "spec-package-boards-element-package-boards-board-feature"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/feature"
summary: "This element contains information about the features and capabilities of a board. A list of pre-defined features exists."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about the features and capabilities of a board. 
A list of pre-defined features exists.

**Example**
```
<feature type="PWR" n="3" m="5" name="Element: Board feature"/>
```

 		



  | 
    Parent | 
    Chain | 
  

  | 
    board | 
    element_board | 
  
	
  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    type | 
    Defines board features. Select predefined values from the table Board Features. | 
    BoardFeatureTypeEnum | 
    required | 
  

  | 
    n | 
    Depends on attribute **\b** type. Check table Board Features for details. | 
    xs:string | 
    optional | 
  

  | 
    m | 
	Depends on attribute **\b** type. Check table Board Features for details. | 
	xs:string | 
	optional | 
  

  | 
    name | 
	Descriptive name of the feature. If omitted, a **Default Name** is used (refer to table
	    Board Feature Types). **Do not repeat** the `n` or `m` values in the name. This will lead to
		duplicate entries on web sites (they show `n` x `name`). | 
	xs:string | 
	optional | 
  




 

 **Table: Board Features**

The table below lists predefined board features.

**Note:**
- The attribute _name_ of the element element_board_feature is a descriptive text for a feature. If _name_ is omitted, the **Default Name** (listed below) is used.
- **Do not repeat** the _n_ or _m_ values in the _name._ Display on websites follows the rule to show _n_ x _name._
- All numbers are a decimal value. Hexadecimal numbers are not supported.


|type=|n=|m=|Default Name|Example|Example shown as|
|-----|--|--|------------|-------|----------------|
|ODbg|Number of Debug Adapters|N/A|Integrated Debug Adapter|\`<feature type="ODbg" n="1" name="Integrated ST-Link on USB Connector J13"/\>`|1 x Integrated ST-Link on USB Connector J13|
|XTAL|Oscillator Frequency|N/A|Crystal Oscillator|\`<feature type="XTAL" n="8000000"/\>`|8 MHz Crystal Oscillator|
|PWR|Minimum Input Voltage|Maximum Input Voltage|Power Supply|\`<feature type="PWR" n="8" m="12"/\>`|8 V - 12 V Power Supply|
|PWRSock|Number of Power Sockets|N/A|Power Socket|\`<feature type="PWRSock" n="1" name="Coaxial Power Receptacle"/\>`|1 x Coaxial Power Receptacle|
|Batt|Number of Batteries|N/A|Battery|\`<feature type="Batt" n="1" name="CR2032 Battery for RTC"/\>`|1 x CR2032 Battery for RTC|
|Curr|Typical Current|Maximum Current|Current|\`<feature type="Curr" n="0.320" m="0.375"/\>`|320 mA (typ), 375 mA (max) Current|
|CoreOther|Number of Features|N/A|Other Core Feature|\`<feature type="CoreOther" n=1 name="My Other Core Feature"/\>`|1 x My Other Core Feature|
|RAM|Number of RAMs|N/A|RAM|\`<feature type="RAM" n="1" name="512 kB Static RAM"/\>`|1 x 512 kB Static RAM|
|ROM|Number of ROMs|N/A|Flash|\`<feature type="ROM" n="1" name="4 MB NAND-Flash"/\>`|1 x 4 MB NAND-Flash|
|Memory|Number of Additional Memory|N/A|Memory|\`<feature type="Memory" n="128" name="EEPROM"/\>`|128 byte EEPROM|
|MemCard|Number of Card Holders|N/A|SD/microSD/MMC Card Holder|\`<feature type="MemCard" n="2" name="SD Card Holder"/\>`|2 x SD Card Holder|
|MemoryOther|Number of Other Memory|N/A|Other Memory Type|\`<feature type="MemoryOther" n="1" name="1 kB MRAM"/\>`|1 x 1 kB MRAM|
|DIO|Number of Digital I/Os|N/A|Digital I/Os|\`<feature type="DIO" n="26" name="Digital IOs on 2 x 13 pin header (1.27 mm pitch)"/\>`|26 x Digital IOs on 2 x 13 pin header (1.27 mm pitch)|
|AIO|Number of Analog I/Os|N/A|Analog I/Os|\`<feature type="AIO" n="4" name="Analog Inputs on 4 pin header (1.27 mm pitch)"/\>`|4 x Analog Inputs on 4 pin header (1.27 mm pitch)|
|Proto|n Rows|m Columns|Prototyping Area|\`<feature type="Proto" n="4" m="7" name="Prototyping Area with 1.00 mm pitch"/\>`|4 x 7 Prototyping Area with 1.00 mm pitch|
|USB|Number of USB Connectors|N/A|USB|\`<feature type="USB"  n="2" name="Full-Speed USB Device, Micro-B receptacle"/\>`|2 x Full-Speed USB Device, Micro-B receptacle|
|ETH|Number of Ethernet Connectors|Data Rate in Bit/s|Ethernet|\`<feature type="ETH"  n="1" m="10000000" name="RJ45 Receptacle"/\>`|1 x 10 Mbit/s RJ45 Receptacle|
|SPI|Number of SPI Connectors|N/A|SPI|\`<feature type="SPI"  n="1" name="4-Pin Header, 1.27 mm Pitch"/\>`|1 x 4-Pin Header, 1.27 mm Pitch|
|I2C|Number of I2C Connectors|N/A|I2C|\`<feature type="I2C"  n="1" name="2-Pin Header, 1.27 mm Pitch"/\>`|1 x 2-Pin Header, 1.27 mm Pitch|
|RS232|Number of RS232 Connectors|N/A|RS232|\`<feature type="RS232"  n="1" name="DB9 Male Connector"/\>`|1 x DB9 Male Connector|
|RS422|Number of RS422 Connectors|N/A|RS422|\`<feature type="RS422"  n="1" name="4-Pin Header, 1.27 mm Pitch"/\>`|1 x 4-Pin Header, 1.27 mm Pitch|
|RS485|Number of RS485 Connectors|N/A|RS485|\`<feature type="RS485"  n="1" name="DB9 Male Connector"/\>`|1 x DB9 Male Connector|
|CAN|Number of CAN Connectors|N/A|CAN|\`<feature type="CAN"  n="1" name="DB9 Male Connector"/\>`|1 x DB9 Male Connector|
|IrDA|Number of IrDA Diodes|N/A|Diode|\`<feature type="IrDA"  n="1" name="Diode Transceiver"/\>`|1 x Diode Transceiver|
|LineIn|Number of Line In Jacks|N/A|Line In|\`<feature type="LineIn"  n="1" name="TRS Audio Jack"/\>`|1 x TRS Audio Jack|
|LineOut|Number of Line Out Jacks|N/A|Line Out|\`<feature type="LineOut"  n="1" name="TRS Audio Jack"/\>`|1 x TRS Audio Jack|
|MIC|Number of Microphone Jacks|N/A|Microphone|\`<feature type="MIC"  n="1" name="TS Audio Jack (Mono)"/\>`|1 x TS Audio Jack (Mono)|
|Edge|n Rows|m Columns|Edge|\`<feature type="Edge"  n="2" m="24"/\>`|2 x 24 Pin Edge|
|ConnOther|Number of Other Connectors|N/A|Other Connector Type|\`<feature type="ConnOther"  n="1" name="My Other Connector"/\>`|1 x My Other Connector|
|Button|Number of Push-Buttons|N/A|Push-buttons|\`<feature type="Button"  n="3" name="Push-buttons: Reset, Wake Up, User"/\>`|3 Push-buttons: Reset, Wake Up, User|
|Poti|Number of Potentiometer|N/A|Potentiometer|\`<feature type="Poti"  n="1"/\>`|1 x Potentiometer|
|Joystick|Number of Joysticks|N/A|Joystick|\`<feature type="Joystick"  n="1" name="5-position Joystick"/\>`|1 x 5-position Joystick|
|Touch|Number of Touch Keys|N/A|Touch Keys/Area|\`<feature type="Touch"  n="1"/\>`|1 x Touch Keys/Area|
|ContOther|Number of Other Controls|N/A|Other Control|\`<feature type="ContOther" n=1 name="My Other Control Feature"/\>`|1 x My Other Control Feature|
|Accelerometer|Number of Accelerometer|N/A|Accelerometer|\`<feature type="Accelerometer"  n="1" name="3-axis digital Accelerometer"/\>`|1 x 3-axis digital Accelerometer|
|Gyro|Number of Gyroscopes|N/A|Gyroscope|\`<feature type="Gyro"  n="1" name="3-axis digital Gyroscope"/\>`|1 x 3-axis digital Gyroscope|
|Compass|Number of Compass|N/A|Digital Compass|\`<feature type="Compass"  n="1" name="High-Precision Digital Compass"/\>`|1 x High-Precision Digital Compass|
|TempSens|Number of Temperature Sensors|N/A|Temperature Sensor|\`<feature type="TempSens"  n="1"/\>`|1 x Temperature Sensor|
|PressSens|Number of Pressure Sensors|N/A|Pressure Sensor|\`<feature type="PressSens"  n="1"/\>`|1 x Pressure Sensor|
|LightSens|Number of Light Sensors|N/A|Ambient Light Sensor|\`<feature type="LightSens"  n="1"/\>`|1 x Ambient Light Sensor|
|SensOther|Number of Other Sensors|N/A|Other Sensor|\`<feature type="SensOther" n=1 name="My Other Sensor Feature"/\>`|1 x My Other Sensor Feature|
|CustomFF|x [mm]|y [mm]|Custom Formfactor|\`<feature type="CustomFF" n="54" m="26" name="40-Pin DIP with 0.1-inch Pitch"/\>`|54 mm x 26 mm, 40-Pin DIP with 0.1-inch Pitch|
|ArduinoFF|1|N/A|Arduino Formfactor|\`<feature type="ArduinoFF"  n="1"/\>`|Arduino Formfactor|
|FreedomFF|1|N/A|Freedom Formfactor|\`<feature type="FreedomFF"  n="1"/\>`|Freedom Formfactor|
|TowerFF|1|N/A|Tower Formfactor|\`<feature type="TowerFF"  n="1"/\>`|Tower Formfactor|
|LED|Number of LEDs|N/A|LEDs|\`<feature type="LED"  n="3" name="Multicolor LEDs"/\>`|3 x Multicolor LEDs|
|Camera|Number of Camera Interfaces|N/A|Camera|\`<feature type="Camera"  n="1" name="Digital VGA Camera"/\>`|1 x Digital VGA Camera|
|LCD|Number of Segment LCD Controller|Com.Seg as a decimal number (see example)|LCD|\`<feature type="LCD"  n="1" m="16.40" name="Segment LCD Controller"/\>`|1 x 16 x 40  Segment LCD Controller|
|GLCD|Number of Graphic LCD Controller|Maximum Resolution as a decimal number (see example)|GLCD|\`<feature type="GLCD"  n="1" m="320.240" name="2.4 inch Color TFT LCD with resistive touchscreen"/\>`|320 x 240 Pixel 2.4 inch Color TFT LCD with resistive touchscreen|
|Speaker|Number of Speakers|N/A|Speaker|\`<feature type="Speaker"  n="1"/\>`|1 x Speaker|
|VirtualHW|1|N/A|Arm Virtual Hardware|\`<feature type="VirtualHW"  n="1"/\>`|Arm Virtual Hardware|
|Other|Number of Other Features|N/A|Other Feature|\`<feature type="Other" n=1 name="My Other Feature"/\>`|1 x My Other Feature|
