---
id: "spec-package-part-taxonomy-element-package-part-taxonomy-description"
type: "concept"
domain: "pack"
title: "/package/part-taxonomy element: /package/part-taxonomy/description"
summary: "This element describes a part class or the combination between a part class and a part group. Parts are categorized by Hclass and Hgroup. The creator of a package can define names for Hclass and Hgroup."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_part-taxonomy.html"
license: "Apache-2.0"
mode: "V"
---

This element describes a part class or the combination between a part class and a part group.
Parts are categorized by **Hclass** and **Hgroup.** The creator of a package can define names for **Hclass** and
**Hgroup.** Thus, configuration tools can display the set of available parts. A document can be referenced using the
attribute **doc.** The attribute **generator** can be used to reference to a generator tool. The **id** of the generator
needs to be the same as specified in the element element_generator. The description itself is a string entered between
the opening and closing tags of the element **description.**

It is recommended to use an already agreed part-taxonomy for interchangeable parts.


 

**Example:**
```
  <part-taxonomy>
    <description Hclass="Audio ICs">Audio Amplifiers, Audio Processors, MEMS Microphones, Sound Terminal Digital Audio Subsystem</description>
    <description Hclass="Automotive" Hgroup="Logic ICs">Buffers/Drivers, Counters/Encoders/Decoders, FlipFlop/registers, Gates, ...</description>
  </part-taxonomy>
```

**Note:** You **must** **not** use Windows or Linux
reserved characters for
**Hclass,** **Hgroup,** and **Hsub** names! Reserved characters are:
```
< (less than)
> (greater than)
: (colon)
" (double quote)
/ (forward slash)
\ (backslash)
| (vertical bar or pipe)
? (question mark)
(asterisk)
```


 



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| element_part-taxonomy "part-taxonomy" | element_part-taxonomy |  |  |
| Attributes | Description | Type | Use |
| Hclass | Part Class Name. Can be defined by the creator of the package. Predefined values can be used as listed in the table Part Classes. | HclassType | required |
| Hgroup | Part Group Name. Can be defined by the creator of the package. Predefined values can be used as listed in the table Part Groups. | HgroupType | optional |
| doc | Reference to documentation. | xs:string | optional |
| generator | Reference to a generator. Enter the **id** value of the element element_generator. | xs:string | optional |
| public | Set publishing permissions for the documentation. If \tagem{public} is `true`, then the vendor gives permission to extract the documentation from the pack and publish it on a web-page. Links to web pages are assumed to be public. The default value is `true` (this is also the basic assumption if the tag is missing). | xs:boolean | optional |




 
 **Table: Part Classes and Groups**

Part Class and Part Group names are strings with a minimum length of 3 characters and a maximum length of 32 characters.
Part Class and Part Group names are specified in the section element_part-taxonomyDescription.
Part Group names are specified by the element **Hgroup** and create categories within a Part Class specified by the element **Hclass**.

Part Classes and Part Groups can be used in the elements:
- element_part
- element_part-taxonomyDescription

**Example:**
```
  <... Hclass="MEMS and Sensors" Hgroup="MEMS Microphone" ...>
```

 

The following table lists predefined Part Classes. Within each Part Class, some Part Groups have been also defined.


| Hclass= | Description | Hgroup= (Description) | Hgroup= (Description) | Hgroup= (Description) | Hgroup= (Description) | Hgroup= (Description) | Hgroup= (Description) |
|---|---|---|---|---|---|---|---|
| Amplifiers and Comparators | Operational amplifiers, Power Operational Amplifiers, Video Amplifiers and Current Sense Amplifiers, Comparators | Comparators | Current Sensing | Op Amp | Power Op Amp | Video Amplifiers |  |
| Audio ICs | Audio Amplifiers, Audio Processors, MEMS Microphones, Sound Terminal Digital Audio Subsystem | Amplifiers | MEMS Sensor | Processors | Sound Terminal ICs |  |  |
| Automotive | Automotive Devices (for Advanced Driver Assistance Systems (ADAS), Analog and Power, Infotainment and Telematics, Logic ICs, Microcontrollers) | ADAS (Advanced Driver Assistance Systems) | Analog and Power | Infotainment and Telematics | Logic ICs (Buffers/Drivers, Counters/Encoders/Decoders, FlipFlop/registers, Gates, ...) | Microcontrollers |  |
| Clocks and Timers | Real-Time Clock (RTC) ICs | RTC | Timers |  |  |  |  |
| Data Converters | A/D - D/A Converters, Isolated ADCs, Metering ICs | A2D - D2A | Isolated ADCs | Metering ICs |  |  |  |
| Digital Set-Top Box ICs | Demodulators and Tuners, Set-Top-Box Processors | Demodulators and Tuners | Set-Top-Box Processors |  |  |  |  |
| Diodes and Rectifiers | Automotive-grade qualified diodes and rectifiers, bridge rectifier diodes, field effect rectifiers, Schottky barrier diodes, Silicon Carbide diodes, ultrafast rectifiers, … | Diodes | Rectifiers |  |  |  |  |
| Imaging and Photonics Devices | Ambient Light sensors, Image sensors, Imaging processors, Time-of-Flight sensors | Ambient Light Sensors | Image Sensors | Imaging Processors | Time-of-Flight Sensors |  |  |
| Interfaces and Transceivers | Standard interfaces (such as RS-232, RS-422, RS-423, RS-485, LVDS, and USB), I/O expanders, level translators, application-specific interfaces for smart cards and Ethernet, and IO-Link Transceivers | Interfaces | I/O Expanders | Level Translators | Transceivers |  |  |
| Memories | EEPROM, FLASH, RAM, … | EEPROM | Flash | RAM |  |  |  |
| MEMS and Sensors | Accelerometers, magnetometers, gyroscopes, environmental sensors, inertial modules, infrared sensors, MEMS microphones | Environmental (Temperature, Humidity, Pressure, …) | Infrared (Sensors for object movement detection and human presence sensing) | MEMS Hybrid (Sensors with both environmental and motion features) | MEMS Microphone | MEMS Motion (Accelerometers, magnetometers, gyroscopes) | Proximity (Time-of-Flight, ...) |
| Motor Drivers | Brushed and brushless motor drivers, stepper motor drivers | Brushed | Brushless | Gate Drivers | Stepper |  |  |
| NFC | NFC / RFID tags and readers, NFC controllers | Secure | Reader | Tag | Tag and Reader |  |  |
| Other | To be used for devices not listed here |  |  |  |  |  |  |
| Positioning | Global Navigation Satellite System (GNSS) modules | GNSS ICs | GNSS Modules |  |  |  |  |
| Power Management | ST's Power Management ICs enable energy-saving, high-power-density and lower-standby-power design solutions (Power ICs, AC-DC converters, switching DC-DC converters, linear voltage regulators, battery management ICs, LED drivers, photovoltaic ICs, MOSFET and IGBT drivers, motor drivers, ...) | AC-DC Converters | Battery Management ICs | DC-DC Switching Converters | Display Supplies and Controllers | eFuses and hot-swap ICs | Energy Harvesting |
| GaN Power ICs | Gate Drivers | High-Density Power Drivers | Intelligent Power Switches | LED Drivers | Lighting ICs |  |  |
| Linear Voltage Regulators | LNB Supplies | Photovoltaic ICs | Power Over Ethernet ICs | Voltage References | Wireless Charger ICs |  |  |
| Power Modules | Power modules for solutions ranging from tens of watts to several kilowatts | ACEPACK | SLLIMM |  |  |  |  |
| Power Transistors | Transistors for high- and low-voltage applications (power MOSFETs , power IGBTs , power bipolar transistors, …) | IGBTs | Bipolar | MOSFETs | Wide Bandgap |  |  |
| Protections | Devices for safe electronic systems and immunity from electromagnetic interference (EMI) | ASIP (Application-Specific Integrated Products) | EMI Filters (Electromagnetic interference filters) | TSS (Thyristor surge suppressor) | TVS (Transient Voltage Suppressors) |  |  |
| Radio Frequency | Radio Frequency power devices (e.g. transistors for Industrial, Scientific and Medical (ISM), for FM and TV Broadcast, for Mobile and wideband communications, for Avionics and Radar, for Telecom and Satellite Communications, …) | RF DMOS | RF LDMOS |  |  |  |  |
| Reset and Supervisor ICs | Microprocessor supervisors and reset ICs for keeping application processor under control (e.g. microprocessor supervisors, resets, voltage detectors, voltage protection ICs, ...) | Microprocessor Supervisors | On-Off Controllers | Reset and Voltage Detectors | Smart Reset ICs | Voltage Protection ICs | Watchdog Timers |
| Secure MCUs | Secure devices for privacy and data confidentiality and integrity protection (secure NFC, SIM, eSIM, …) | Authentication | Secure | SIM |  |  |  |
| SiC Devices | Silicon Carbide (SiC) devices (e.g. diodes, MOSFET, …) for efficient energy handling | SiC Diodes | SiC MOSFETs |  |  |  |  |
| Space Devices | Devices for aerospace applications designed to be compliant with the standards for aerospace (e.g. the American QML-V standard of the US DLA - Defense Logistics Agency, the RHA - Radiation Hardness Assurance certification) | LEO Rad-Hard ICs (Low Earth Orbit Radiation Hardness ICs) | Rad-Hard Analog ICs | Rad-Hard ASIC Platforms | Rad-Hard Discretes | Rad-Hard Interfaces | Rad-Hard Logic ICs |
| Rad-Hard Power Management |  |  |  |  |  |  |  |
| Switches and Multiplexers | Switches (analog, data signal, power/load switches) and multiplexers for audio/video applications and ultrasound imaging | Switches | Multiplexers |  |  |  |  |
| Thyristors and AC Switches | Thyristors (aka Silicon-Controlled Rectifiers), Triacs and AC Switches (they are power devices) | Switches | Thyristors | Triacs |  |  |  |
| Touch and Display Controllers | Touch-screen controllers for multi-touch user interfaces (UIs) |  |  |  |  |  |  |
| Wireless | Wireless connectivity devices for IoT, to remotely monitor, configure and control appliances and evices, to replace cable and connectors with wireless communications (e.g. 6LoWPAN devices, LoRaWAN devices, Bluetooth Low Energy devices, Ultra-wideband devices, ...) | Long Range (6LoWPAN, KNX-RF, LoRaWAN, Sub-1 GHz, Sigfox, Wi-Sun, Wireless M-BUS, …) | RF Front-end (Baluns, Filters, ...) | RF Solutions (RF PLL Synthesizers, ...) | Short Range (60 GHz Contactless, Bluetooth Low Energy, Thread, Ultra Wideband, ZigBee, Wi-Fi, ...) |  |  |
