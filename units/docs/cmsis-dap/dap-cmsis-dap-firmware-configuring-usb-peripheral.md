---
id: "dap-cmsis-dap-firmware-configuring-usb-peripheral"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Configuring USB peripheral"
summary: "CMSIS-DAP firmware communicates via USB with the host computer. The USB communication is implemented via Keil MDK-Middleware components that access the USB peripheral of the microcontroller."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

CMSIS-DAP firmware communicates via USB with the host computer. The USB communication is implemented via Keil MDK-Middleware components that access the USB peripheral of the microcontroller.

The CMSIS-DAP v2 firmware uses USB bulk endpoints that provide high-speed communication. In addition, dap_usb_cdc is used to enable USB COM port.

For the USB interface it is important to provide correct configuration information for the USB peripheral as described in this section.

The following steps describe how to change and configure the USB peripheral in the CMSIS-DAP firmware project:

 1. In the **Project Window**, the group **USB** contains USB interface with the relevant configuration files.
 2. Open the file `usb_config_0.c` in the editor and select **Configuration Wizard** as edit mode; then change the following settings:
  - **USB Device 0 - High-speed**: enable this option only for a high-speed USB peripheral; disable for full-speed USB.
  - Update **Device Settings - Vendor ID** which is provided by the [USB Implementers Forum](https://www.usb.org/getting-vendor-id).
  - Update **Device Settings - Product ID** to provide a unique identification for the debug unit.
  - Update **Device Settings - Device Release Number** to indicate the revision of the adaptation.
  - Update **String Settings - Manufacturer String** to reflect the vendor of the debug unit. This setting should match the **Vendor ID**.
  - Update **String Settings - Product String** to indicate the debug unit. Note that "CMSIS-DAP" must be part of that string to allow identification by debuggers (or part of interface string for USB composite device).
  - Optionally each debug unit may provide a unique **Serial Number String**. If the **String Settings - Serial Number String** is not provided, only one debug unit can be connected at the same time to a host computer since it is impossible to identify multiple debug units.

> **Note**
>  - The USB Device setting high-speed / full-speed USB must be reflected in the `DAP_config.h` file.
>  - The **String Settings - Product String** must contain "CMSIS-DAP" somewhere in the string. This is used by the debuggers to identify a CMSIS-DAP compliant debug unit that is connected to a host computer.

(figure: Adapt the USB Peripheral to the microcontroller)

### Communication via USB bulk endpoints

CMSIS-DAP v2 uses USB bulk endpoints. Optionally, support for streaming SWO trace is provided via an additional USB endpoint.

This configuration requires custom class support with the interface setting:

 - Class Code: `0xFF` (Vendor specific)
 - Subclass: `0x00`
 - Protocol code: `0x00`

> **Note**
> - This interface enables also [WebUSB](https://wicg.github.io/webusb/) technology that is used in web browsers to connect to a debug adapter connected to your PC.

Depending on the configuration, it uses the following USB endpoints which should be configured in the interface descriptor in this order:

 - Endpoint 1: Bulk Out – used for commands received from host PC.
 - Endpoint 2: Bulk In – used for responses send to host PC.
 - Endpoint 3: Bulk In (optional) – used for streaming SWO trace (if enabled with SWO_STREAM).

(figure: Configuration settings for the USB custom class)

> **Note**
> - These settings allow support in Windows (8 and above), Mac OS, and Linux without further drivers. Some additional settings are required to automatically install CMSIS-DAP enabled debug adapters in these operating systems.

**Additional settings for Microsoft Windows**

For automatic installation of a CMSIS-DAP v2 enabled debug adapter in Windows, use the following WinUSB GUID in the USB custom class:

```
{CDB3B5AD-293B-4663-AA36-1AAE46463776}
```

The picture below shows the WinUSB GIUD configuration of the USB custom class:

(figure: Adapt CMSIS-DAP to the WinUSB class)


**USB Driver**

Windows 8 and above does not require a WinUSB driver provided that the USB firmware stack supports Microsoft descriptors.

CMSIS-DAP v2 device should be configured as WCID (Windows Compatible ID) device which provides extra information to a Windows system to facilitate automated driver installation.

Also see dap_drv_install for additional information.

### Communication Device Class

CMSIS-DAP v2 supports also a UART communication port optionally routed to a USB COM port which is implemented by a USB Communication Device Class (CDC) device.

The picture below shows the configuration of the USB CDC class.

(figure: Configuration of USB CDC class)
