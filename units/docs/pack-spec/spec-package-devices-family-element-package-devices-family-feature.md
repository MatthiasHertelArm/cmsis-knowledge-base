---
id: "spec-package-devices-family-element-package-devices-family-feature"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../feature"
summary: "This element specifies peripherals that devices can have. This can be used on web sites for the display of device features."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies peripherals that devices can have. This can be used on **web** **sites** for the display of device
features.

Many device feature types are already predefined, such as timers, converters, Ethernet, USB, etc (for a complete list refer
to table Device Feature Types). Features can be defined on various levels. Inner elements
supersede outer elements.

This element can be used also to describe information about the features and capabilities of a package/parts/part. 
The list of the pre-defined features for Devices (Device Feature Types) can be used also for parts. 

**Example**
```
<package>
  <devices>
    <family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
      ...
      <!--  Features that are in common to this device family. -->
      <feature type="TimerOther" n="1" name="Independent Watchdog Timer"/>
      <feature type="TimerOther" n="1" name="Window Watchdog Timer"/>          <!-- The same feature type can be specified multiple times -->
      <feature type="Other" n="1" name="Temperature Sensor"/>
      <feature type="CoreOther" n="1" name="96-bit Unique Identifier"/>
      <feature type="CoreOther" n="1" name="CRC Calculation Unit"/>
      <feature type="DMA" n="16" name="General Purpose DMA with Centralized FIFO and Burst Support"/>
      <feature type="PowerOther" n="1" name="POR, PDR, PVD, and BOR"/>
      <feature type="XTAL" n="4000000" m="26000000" name="Crystal Oscillator"/>
      <feature type="IntRC" n="16000000" name="Internal Factory-Trimmed RC"/>
      <feature type="IntRC" n="32000" name="Internal RC with Calibration"/>
      <feature type="RTC" n="32000" name="RTC with 32 kHz calibrated Oscillator and Battery Backup"/>
      <feature type="PowerMode" n="3" name="Run, Stop, Standby"/>
      <feature type="Temp" n="-40" m="85"/> 
      <feature type="Temp" n="-40" m="105"/> 
      <feature type="Timer" n="4" m="16" name="General Purpose Timer"/>
      ...
      <subFamily DsubFamily="STM32F407">
        <!--  Features that are in common to this subFamily. -->
        <feature type="IOs" n="36"/>                                                  <!-- Adds new feature to subFamily  -->
        <feature type="Timer" n="7" m="32" name="General Purpose Timer"/>             <!-- Adds to settings from <family> -->

        
        <device Dname="STM32F407IE">
          <!--  Feature specific to this device.  All above features are inherited.  -->
          <feature type="QFP" n="176" name="LQFP 176 24x24x1.4"/>
        </device>
      </subFamily>
    </family>
  </devices>
</package>
```

```
<package>
  ...
  <parts>
    <part Hvendor="STMicroelectronics" Hname="STSAFE-A110" Hvariant="STSAFA110DFSPL02" Hclass="Secure" Hgroup="Authentication">
      <feature type="Crypto" n="128.256" name="Authentication and security for peripherals and IoT devices from STMicroelectronics"/>
      ...
    </part>
    ...
  <\parts>
  ...
<\package>
```

\n



  | 
    Parents | 
    Element Chain | 
  

  | 
    family | 
    element_family | 
  

  | 
    subFamily | 
    element_subFamily | 
  

  | 
    device | 
    element_device | 
  

  | 
    part | 
    element_part | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Pname | 
    Processor Identifier. This attribute **is mandatory for devices that embed multiple processors**.
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.
        


        Must not be used for package/parts/part. | 
    RestrictedString | 
    optional | 
  

  | 
    type | 
    A feature (peripheral), such as `CAN`, `DMA`, `I/O`, `LCD`, etc. Predefined values must be used
        as listed in the table Device Feature Types.
        


        Can be also used to describe the package/parts/part features. Predefined values must be used as listed in the table Device Feature Types. | 
    DeviceFeatureTypeEnum | 
    required | 
  

  | 
    n | 
    Depends on the element **\b** type. Check table Device Feature Types. | 
    xs:string | 
    optional | 
  

  | 
    m | 
    Depends on the elemen **\b** type. Check table Device Feature Types. | 
    xs:string | 
    optional | 
  

  | 
    name | 
    Descriptive name of the feature. For example, "16-bit down counting timer". If omitted, the **Default Name** is used 
    as described in the table Device Feature Types. | 
    xs:string | 
    optional | 
  



\n

 **Table: Device Feature Types**

The table lists predefined device features (peripherals).
**Note:**
- The attribute _name_ of the element element_feature is a descriptive text for a feature. If _name_ is omitted, then the **Default Name** is used.
- All numbers are a decimal value. Hexadecimal numbers are not supported.

type=|n=|m=|Default Name|Example|Example shown as |
-----|--|--|------------|-------|---------------- |
NVIC|Number of NVIC Interrupts|N/A|NVIC|\`<feature type="NVIC" n="120" name="NVIC"/\>`|NVIC with 120 interrupt sources|
DMA|Number of DMA Channels|N/A|DMA|\`<feature type="DMA" n="16" name="High-Speed DMA"/\>`|16-channel High-Speed DMA|
Crypto|Bitwidth, given as decimal Number (see example)|N/A|Cryptographic Engine|\`<feature type="Crypto" n="128.256" name="HW accelerated AES Encryption Engine"/\>`|128/256-bit HW accelerated AES Encryption Engine|
RNG|Number of RNGs|N/A|Random Number Generator|\`<feature type="RNG" name="True Random Number Generator"/\>`|True Random Number Generator|
CoreOther|Number of Features|N/A|Other Core Feature|\`<feature type="CoreOther" n=1 name="96-bit Unique Identifier"/\>`|1 x 96-bit Unique Identifier|
Memory|Number of Bytes|N/A|Memory|\`<feature type="Memory" n="128" name="EEPROM"/\>`|128 byte EEPROM|
MemoryOther|Number of Memories|N/A|Other Memory Type|\`<feature type="MemoryOther" n="1" name="1 kB MRAM"/\>`|1 x 1 kB MRAM|
ExtBus|Bitwidth of Bus Interface|N/A|External Bus Interface|\`<feature type="ExtBus" n="16" name="External Bus Interface for SRAM Communication"/\>`|16-bit External Bus Interface for SRAM Communication|
XTAL|Minimum Frequency in Hz|Maximum Frequency in Hz|External Crystal Oscillator|\`<feature type="XTAL"  n="4000000" m="25000000" name="External Crystal Oscillator"/\>`|4 MHz .. 25 MHz External Crystal Oscillator|
IntRC|Minimum Frequency in Hz|Maximum Frequency in Hz|Internal RC Oscillator|\`<feature type="IntRC"  n="16000000" name="Internal RC Oscillator with +/- 1% accuracy"/\>`|16 MHz Internal RC Oscillator with +/- 1% accuracy|
PLL|Number of PLLs|N/A|PLL|\`<feature type="PLL"  n="3" name="Internal PLL"/\>`|3 Internal PLL|
RTC|RTC Frequency|N/A|RTC|\`<feature type="RTC"  n="32000" name="Internal RTC"/\>`|32 kHz Internal RTC|
ClockOther|Number of Peripherals|N/A|Other Clock Peripheral|\`<feature type="ClockOther" name="My special clock feature"/\>`|My special clock feature|
PowerMode|Number of Power Modes|N/A|Power Modes|\`<feature type="Mode"  n="3" name="Run, Sleep, Deep-Sleep"/\>`|3 Power Modes: Run, Sleep, Deep-Sleep|
VCC|Minimum Supply Voltage|Maximum Supply Voltage|Operating Voltage|\`<feature type="VCC"  n="1.8" m="3.6"/\>`|1.8 V .. 3.6 V|
Consumption|Minimum Power Consumption|Typical Power Consumption|Power Consumption|\`<feature type="Consumption"  n="0.00004" m="0.002" name="Ultra-Low Power Consumption"/\>`|40 uW/MHz .. 2 mW/MHz Ultra-Low Power Consumption|
PowerOther|Number of Features|N/A|Other Power Feature|\`<feature type="PowerOther" n="1" name="POR"/\>`|1 x POR|
BGA|Number of Balls|N/A|BGA|\`<feature type="BGA" n="256" name="Plastic Ball Grid Array"/\>`|256-ball Plastic Ball Grid Array|
CSP|Number of Leads|N/A|CSP|\`<feature type="CSP" n="28" name="Wafer-Level Chip-Scale Package"/\>`|28-ball Wafer-Level Chip-Scale Package|
PLCC|Number of Leads|N/A|PLCC|\`<feature type="PLCC" n="20" name="PLCC Package"/\>`|20-lead PLCC Package|
QFN|Number of Leads|N/A|QFN|\`<feature type="QFN" n="33" name="QFN Package"/\>`|33-pad QFN Package|
QFP|Number of Leads|N/A|QFP|\`<feature type="QFP" n="128" name="Low-Profile QFP Package"/\>`|128-lead Low-Profile QFP Package|
SON|Number of Leads|N/A|SON|\`<feature type="SON" n="16" name="SSON Package"/\>`|16-lead SSON Package|
SOP|Number of Leads|N/A|SOP|\`<feature type="SOP" n="16" name="SSOP Package"/\>`|16-lead SSOP Package|
DIP|Number of Leads|N/A|DIP|\`<feature type="DIP" n="16" name="Dual In-Line Package"/\>`|16-lead Dual In-Line Package|
PackageOther|Number of Pins|N/A|Other Package Type|\`<feature type="PackageOther"  n="44" name="My other Package"/\>`|44-contacts My other Package|
IOs|Number of I/Os|N/A|Inputs/Outputs|\`<feature type="IOs"  n="112" name="General Purpose I/Os, 5V tolerant"/\>`|112 General Purpose I/Os, 5V tolerant|
ExtInt|Number of External Interrupts|N/A|External Interrupts|\`<feature type="ExtInt"  n="12"/\>`|12 External Interrupts|
Temp|Minimum Operating Temperature|Maximum Operating Temperature|Operating Temperature Range|\`<feature type="Temp"  n="-40" m="105" name="Extended Operating Temperature Range"/\>`|-40 °C .. +105 °C Extended Operating Temperature Range|
ADC|Number of Channels|Resolution in Bit|ADC|\`<feature type="ADC"  n="5" m="12" name="High-Performance ADC"/\>`|5-channel x 12-bit High-Performance ADC|
DAC|Number of Channels|Resolution in Bit|DAC|\`<feature type="DAC"  n="2" m="10"/\>`|2 x 12-bit DAC|
TempSens|Number of Sensors|N/A|Temperature Sensor|\`<feature type="TempSens"  n="1"/\>`|1 x Temperature Sensor|
AnalogOther|Number of Features|N/A|Other Analog Peripheral|\`<feature type="AnalogOther"  n="1" name="My Analog"/\>`|1 x My Analog|
Timer|Number of Channels|Resolution in Bit|Timer/Counter Module|\`<feature type="Timer"  n="2" m="32" name="Timer Module with Quadrature Encoding"/\>`|2 x 32-bit Timer Module with Quadrature Encoding|
PWM|Number of Channels|Resolution in Bit|PWM|\`<feature type="PWM"  n="2" m="16" name="Pulse Width Modulation"/\>`|2 x 16-bit Pulse Width Modulation|
WDT|Number of Watchdogs|N/A|Watchdog|\`<feature type="WDT"  n="1"/\>`|1 x Watchdog Timer|
TimerOther|Number of Features|N/A|Other Timer Peripheral|\`<feature type="TimerOther"  n="1" name="Quadrature En-/Decoder"/\>`|1 x Quadrature En-/Decoder|
MPSerial|Number of Serial Peripherals|N/A|Multi-Purpose Serial Peripheral|\`<feature type="MPSerial"  n="4" name="Multi-Purpose Serial Interface Module: I2C, I2S, SPI, UART"/\>`|4 x Multi-Purpose Serial Interface Module: I2C, I2S, SPI, UART|
CAN|Number of CAN Interfaces|N/A|CAN|\`<feature type="CAN"  n="2" name="CAN 2.0b Controller"/\>`|2 x CAN 2.0b Controller|
ETH|Number of Ethernet Interfaces|Data Rate in Bit/s|Ethernet|\`<feature type="ETH"  n="1" m="10000000" name="Integrated Ethernet MAC with PHY"/\>`|1 x 10 Mbit/s Integrated Ethernet MAC with PHY|
I2C|Number of I2C Interfaces|N/A|I2C|\`<feature type="I2C"  n="2"name="Low-Power I2C"/\>`|2 x Low-Power I2C|
I2S|Number of I2S Interfaces|N/A|I2S|\`<feature type="I2S"  n="3"/\>`|3 x I2S|
LIN|Number of LIN Interfaces|N/A|LIN|\`<feature type="LIN"  n="4"/\>`|4 x LIN|
SDIO|Number of SDIO Interfaces|Bitwidth of SDIO Interface|SDIO|\`<feature type="SDIO"  n="1" m="4" name="SDIO Interface"/\>`|1 x 4-bit SDIO Interface|
SPI|Number of SPI Interfaces|Data Rate in Bit/s|SPI|\`<feature type="SPI"  n="2" m="20000000" name="SPI Interface"/\>`|2 x 20 Mbit/s SPI Interface|
UART|Number of UART Interfaces|Data Rate in Bit/s|UART|\`<feature type="UART"  n="4" m="3000000" name="High-Speed UART Interface"/\>`|4 x 3 Mbit/s High-Speed UART Interface|
USART|Number of USART Interfaces|Data Rate in Bit/s|USART|\`<feature type="USART"  n="2" m="1000000" name="High-Speed USART Interface"/\>`|2 x 1 Mbit/s High-Speed USART Interface|
USBD|Number of USB Dvice Interfaces|N/A|USB Device|\`<feature type="USBD"  n="2" name="Full-Speed USB Device"/\>`|2 x Full-Speed USB Device|
USBH|Number of USB Host Interfaces|N/A|USB Host|\`<feature type="USBH"  n="2" name="High-Speed USB Host"/\>`|2 x High-Speed USB Host|
USBOTG|Number of USB OTG Interfaces|N/A|USB OTG|\`<feature type="USBOTG"  n="1" name="High-Speed USB OTG with PHY"/\>`|1 x High-Speed USB OTG with PHY|
ComOther|Number of other Communication Peripherals|N/A|Other Communication Peripheral|\`<feature type="ComOther"  n="1" name="ZigBee"/\>`|1 x ZigBee|
Camera|Number of Camera Interface|Resolution in Bit|Camera Interface|\`<feature type="Camera"  n="1" m="8" name="Digital Camera Interface"/\>`|1 x 8-bit Digital Camera Interface|
GLCD|Number of Graphic LCD Controller|Maximum Resolution as a decimal number (see example)|Graphic LCD Controller|\`<feature type="GLCD"  n="1" m="320.240" name="TFT LCD Controller"/\>`|1 x 320 x 480 pixel TFT LCD Controller|
LCD|Number of Segment LCD Controller|Com.Seg as a decimal number (see example)|Segment LCD Controller|\`<feature type="LCD"  n="1" m="16.40" name="Segment LCD Controller"/\>`|1 x 16 x 40  Segment LCD Controller|
Touch|Number of Touch Channels|N/A|Capacitive Touch Inputs|\`<feature type="Touch"  n="10" name="Capacitive Touch Inputs"/\>`|10 x Capacitive Touch Inputs|
Other|Number of Features|N/A|Other Feature|\`<feature type="Other"  n="2" name="My other Interface"/\>`|2 x My other Interface|
GPU|IP Name|Number of Shaders|GPU|\`<feature type="GPU" n="Mali G71" m="1024"/\>`|Mali G71 GPU with 1024 Shaders|
AI|N/A|N/A|AI|\`<feature type="AI"/\>`|AI accelerator|
FPGA|Number of Logic Elements|N/A|FPGA Array|\`<feature type="FPGA" n="100000"/\>`|FPGA with 100000 Logic Elements|
Application|Automotive, Industrial, Medical, MilAero|Standard Name|N/A|\`<feature type="Application" n="Automotive" m="ISO 26262"/\>`|Automotive ISO 26262 Applications|
IrDA|Standard Version|Data Rate in Bit/s|Infrared|\`<feature type="IrDA" n="" m="1000000"/\>`|IrDA 1 Mbit/s|
HDMI|Standard Version|N/A|HDMI|\`<feature type="HDMI" n="1.3"/\>`|HDMI 1.3|
MIPI|Standard Version|Data Rate in Bit/s|MIPI|\`<feature type="MIPI" n="CSI" m="5000000000"/\>`|MIPI CSI 5 Gbit/s|
PCIe|Standard Version|Maximum Data Rate in Bit/s|PCIe|\`<feature type="PCIe" n="3.0" m="3000000000"/\>`|PCIe 3.0 3 GT/s|
Bluetooth|Standard Version|Maximum Data Rate in Bit/s|Bluetooth|\`<feature type="Bluetooth" n="4.2" name="Bluetooth Low Energy"/\>`|Bluetooth Low Energy 4.2|
ZigBee|Application Profile|Data Rate in Bit/s|ZigBee|\`<feature type="Zigbee" n="Home Automation 2.1"/\>`|ZigBee Home Automation 1.2|
802.15.4|Standard Version|N/A|802.15.4|\`<feature type="802.15.4" n="802.15.4d"/\>`|802.15.4d|
WiFi|Standard Version|Maximum Data Rate in Bit/s|WiFi|\`<feature type="WiFi" n="802.11ac"/\>`|802.11ac WiFi|
LoRa|Standard Version|Maximum Data Rate in Bit/s|LoRa|\`<feature type="LoRa"/\>`|LoRa|
LTE Cat-M|Standard Version|Maximum Data Rate in Bit/s|LTE Cat-M|\`<feature type="LTE-M" n="M1" m="1000000"/\>`|LTE-M M1 1 Mbit/s|
NB-IoT|Standard Version|Maximum Data Rate in Bit/s|NB IoT|\`<feature type="NB-IoT" n="NB1" m="250000"/\>`|NB-IoT NB1 250 kbit/s|
NFC|Standard Version|Maximum Data Rate in Bit/s|NFC|\`<feature type="NFC" n="ISO 18092"/\>`|NFC ISO 18092|
NPU|Accelerator Type|Optional Value|Neural Processing Unit|\`<feature type="NPU" n="Ethos-U55" m="128MACs"/\>`|Ethos-U55 128MACs|
WirelessOther|Standard Version|Maximum Data Rate in Bit/s|Other Wireless Connectivity|\`<feature type="WirelessOther" n="MyStandard" m="1000000"/\>`|MyStandard 1 Mbit/s Wireless Connectivity|
	
\delim
