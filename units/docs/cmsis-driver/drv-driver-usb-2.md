---
id: "drv-driver-usb-2"
type: "concept"
domain: "drivers"
title: "Driver USB"
summary: "The header file Driver_USBH.h defines the API for the USB Host Driver interface used by middleware components."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USB.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USB.c"
license: "Apache-2.0"
mode: "V"
---

**USB Host API**

The header file **Driver_USBH.h** defines the API for the **USB Host Driver** interface used by middleware components.
The driver implementation itself is a typical part of the Device Family Pack, which provides entry points to the interface 
as function pointers in the struct ARM_DRIVER_USBH. This structure can be available several times in each interface to control multiple USBH interfaces.

**Driver_USBH.h** also defines callback routines, which are categorized in 
**port event callbacks** and **pipe event callbacks**.
Callbacks are called by the driver, in interrupt context when an appropriate event occurs, to signal port related events (ARM_USBH_SignalPortEvent)
and pipe related events (ARM_USBH_SignalPipeEvent). 

\cond

**USB Host Function Call Sequence**

To use the USBH driver invoke the API functions in the following order:

\msc
 a [label="", textcolor="indigo", linecolor="indigo", arclinecolor="red"],
 b [label="", textcolor="blue", linecolor="blue", arclinecolor="blue"];

 a rbox a [label="Middleware", linecolor="indigo"],
 b rbox b [label="USBH Driver", linecolor="blue"];
 a=>b [label="ARM_USBH_Initialize", URL="ARM_USBD_Initialize"];
 --- [label="Repeat and use as needed"];
 --- [label="Repeat End"];
 a=>b [label="ARM_USBH_Uninitialize", URL="ARM_USBH_Uninitialize"];
\endmsc

 

\endcond
