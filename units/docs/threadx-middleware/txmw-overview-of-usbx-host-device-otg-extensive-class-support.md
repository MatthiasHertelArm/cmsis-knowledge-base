---
id: "txmw-overview-of-usbx-host-device-otg-extensive-class-support"
type: "concept"
domain: "rtos"
title: "Overview of USBX: Host, Device, OTG & Extensive Class Support"
summary: "USBX Host/Device embedded USB protocol stack is an Industrial Grade embedded USB solution designed specifically for deeply embedded, real-time, and IoT applications. USBX provides host, device, and OTG support, as well as extensive class support."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/overview-usbx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/overview-usbx.md#host-device-otg-extensive-class-support"
license: "MIT"
mode: "V"
---

USBX Host/Device embedded USB protocol stack is an Industrial Grade embedded USB solution designed specifically for deeply embedded, real-time, and IoT applications. USBX provides host, device, and OTG support, as well as extensive class support. USBX is fully integrated with ThreadX Real-Time Operating System, FileX embedded FAT-compatible file system, and NetX Duo embedded TCP/IP stack. All of this, combined with an extremely small footprint, fast execution and superior ease-of-use, make USBX the ideal choice for the most demanding embedded IoT applications requiring USB connectivity.

### USBX memory footprint

USBX has a remarkably small minimal footprint of 10.5 KB of FLASH and 5.1 KB RAM for USBX Device CDC/ACM support. USBX Host requires a minimum of 18 KB of FLASH and 25 KB of RAM for CDC/ACM support.

An additional 10 KB to 13 KB of instruction area memory is needed for TCP functionality. USBX RAM usage typically ranges from 2.6 KB to 3.6 KB plus the packet pool memory, which is defined by the application.

Like ThreadX, the size of USBX automatically scales based on the services actually used by the application. This virtually eliminates the need for complicated configuration and build parameters, making things easier for the developer.

### USB Interoperability verification

USBX Device Stack has been rigorously tested with the USB IF standard testing tool USBCV to ensure full compliance with the USB specifications and interoperability with different host systems.
In addition, USBX OTG stack has been verified and certified by the independent test lab Allion in Taiwan.

### USB Host controller support

USBX supports major USB standards like OHCI and EHCI. In addition, USBX supports proprietary discrete USB host controllers from Atmel, Microchip, Philips, Renesas, ST, TI, and other vendors. USBX also supports multiple host controllers in the same application.
USB Device controller support
USBX supports popular USB device controllers from Analog Devices, Atmel, Microchip, NXP, Philips, Renesas, ST, TI, and other vendors.

### Extensive Host Class support

USBX Host provides support for most popular classes, including ASIX, AUDIO (1.0/2.0), CDC/ACM, CDC/ECM, GSER, HID (keyboard, mouse, and remote control), HUB, PIMA (PTP/MTP), PRINTER, PROLIFIC, STORAGE and VIDEO.

### Extensive USB Device Class support

USBX Device provides support for most popular classes, including AUDIO (1.0/2.0), CDC/ACM, CDC/ECM, DFU, HID, PIMA (PTP/MTP) (w/MTP), RNDIS, STORAGE, PRINTER, CCID and VIDEO. Support for custom classes is also available.

### Pictbridge support

USBX supports the full Pictbridge implementation both on the host and the device. Pictbridge sits on top of USBX PIMA (PTP/MTP) class on both sides. The PictBridge standard allows the connection of a digital still camera or a smart phone directly to a printer without a PC, enabling direct printing to certain Pictbridge aware printers. When a camera or phone is connected to a printer, the printer is the USB host and the camera is the USB device. However, with Pictbridge, the camera will appear as being the host and commands are driven from the camera. The camera is the storage server, the printer the storage client. The camera is the print client and the printer is of course the print server. Pictbridge uses USB as a transport layer but relies on PTP (Picture Transfer Protocol) for the communication protocol.

### Custom class support

USBX Host and Device support custom classes. An example custom class is provided in the USBX distribution. This simple data pump class is called DPUMP and can be used as a model for custom application classes.
Advanced technology
USBX Host and Device support custom classes. An example custom class is provided in the USBX distribution. USBX is advanced technology that includes:

* Host, Device, and OTG support
* USB low, full, and high-speed support
* Automatic scaling
* Fully integrated with ThreadX, FileX, and NetX Duo
* Optional performance metrics
* TraceX system analysis support
