---
id: "drv-usb-interface"
type: "concept"
domain: "drivers"
title: "USB Interface"
summary: "The Universal Serial Bus (USB) implements a serial bus for data exchange. It is a host controlled, plug-and-play interface between a USB host and USB devices using a tiered star topology."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USB.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USB.c"
license: "Apache-2.0"
mode: "V"
---

USB common definitions (%Driver_USB.h)

The **Universal Serial Bus** (USB) implements a serial bus for data exchange. It is a host controlled, plug-and-play interface
between a USB host and USB devices using a tiered star topology. 
In microcontroller (MCU) applications, the interface is often used to connect a device to a host for data exchange or control purposes.

 - Wikipedia offers more information about the **Universal Serial Bus**.
 - The USB Implementers Forum provides detailed documentation under **www.usb.org**.


**Block Diagram**

Typically only one USB Device is connected to a USB Host. If several USB devices must be connected to the same USB host, then
the connection must be done via a USB hub.



 "Simplified USB Schema"



**USB API**

The following header files define the Application Programming Interface (API) for the USB interface:
  - **%Driver_USB.h** :  Common definitions of the USBD and USBH interface
  - **%Driver_USBD.h** : Driver API for USB Device Peripheral
  - **%Driver_USBH.h** : Driver API for USB Host Peripheral

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_USBD : access struct for USBD driver functions
  - ARM_DRIVER_USBH : access struct for USBH driver functions
