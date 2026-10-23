---
id: "drv-wifi-interface"
type: "concept"
domain: "drivers"
title: "WiFi Interface"
summary: "Wi-Fi is technology for radio wireless local area networking of devices. Wi-Fi compatible devices typically connect to the Internet via a WLAN and a wireless access point (AP) also called hotspot."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for WiFi (%Driver_WiFi.h)
 

Wi-Fi is technology for radio wireless local area networking of devices. Wi-Fi compatible devices typically
connect to the Internet via a WLAN and a wireless access point (AP) also called hotspot.

Wikipedia offers more information about 
the **WiFi**.

**Driver Block Diagram**

  "Block Diagram of the WiFi interface"

**WiFi API**

The following header files define the Application Programming Interface (API) for the WiFi interface:
  - **%Driver_WiFi.h** : Driver API for WiFi

The CMSIS-Driver WiFi provides access to the following interfaces:

 - Control interface: setup and control the WiFi module.
 - Management interface: allows you to configure and manage the connection
   to the WiFi access point (AP) or configure and manage the access point (AP).
 - Socket interface: provides the interface to an IP stack that is running
   on the WiFi module. This IP stack handles data communication.
 - Bypass interface: is an optional interface and enables the transmission of
   Ethernet frames with the WiFi module. Using this interface requires the IP stack running on the microcontroller.
   **Note:** Often, WiFi chips and modules have their own networking stack incorporated. This means that payload data is sent via
a serial interface (SPI or USART) to the WiFi chip/module and the Ethernet frames are assembled inside. If you intend to use
a separate TCP/IP stack on the microcontroller, make sure that the WiFi driver has a wifi_bypass_gr.
This allows to send the Ethernet frames assembled by the TCP/IP component transparently through the WiFi chip/module.

The WiFi interface usually requires CMSIS-RTOS features (i.e. mutex) and is often implemented
with a peripheral device that is connected to the system using the SPI or UART interface. However,
there are also some microcontroller devices with WiFi interface on the chip.

The implementation of the WiFi CMSIS-Driver is therefore generally provided as a separate software pack.
It is often implemented as wrapper to the SDK (Software Development Kit) of the WiFi chipset.

**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_WIFI : access struct for WiFi driver functions
