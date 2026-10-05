---
id: "drv-driver-usb"
type: "concept"
domain: "drivers"
title: "Driver USB"
summary: "The header file DriverUSBD.h defines the API for the USB Device Driver interface used by middleware components."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USB.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USB.c"
license: "Apache-2.0"
mode: "V"
---

**USB Device API**

The header file **Driver_USBD.h** defines the API for the **USB Device Driver** interface used by middleware components.
The driver implementation itself is a typical part of the Device Family Pack, which provides entry points to the interface 
as function pointers in the struct ARM_DRIVER_USBD. This structure can be available several times in each interface to control multiple USBD interfaces.

Header file **Driver_USBD.h** also defines callback routines that can be categorized as 
**device event callbacks** and **endpoint event callbacks**.
Callbacks are called by the driver, in interrupt context when an appropriate event occurs, to signal device related events (USBD_dev_events)
and endpoint related events (USBD_ep_events).


**USB Device Function Call Sequence**

To use the USBD driver invoke the API functions in the following order:

\msc
 a [label="", textcolor="indigo", linecolor="indigo", arclinecolor="red"],
 b [label="", textcolor="blue", linecolor="blue", arclinecolor="blue"];

 a rbox a [label="Middleware", linecolor="indigo"],
 b rbox b [label="USBD Driver", linecolor="blue"];
 a=>b [label="ARM_USBD_Initialize", URL="ARM_USBD_Initialize"];
 a=>b [label="ARM_USBD_PowerControl (ARM_POWER_FULL)", URL="ARM_USBD_Initialize"];
 a=>b [label="ARM_USBD_DeviceConnect", URL="ARM_USBD_DeviceConnect"];
 a<=b [label="ARM_USBD_SignalDeviceEvent (ARM_USBD_EVENT_RESET)", URL="ARM_USBD_SignalDeviceEvent", linecolor="orange"];
 a=>b [label="ARM_USBD_DeviceGetState", URL="ARM_USBD_DeviceGetState"];
 a=>b [label="ARM_USBD_EndpointConfigure", URL="ARM_USBD_EndpointConfigure", linecolor="green"];
 --- [label="Repeat and use as needed"];
 a=>b [label="ARM_USBD_EndpointTransfer", URL="ARM_USBD_EndpointTransfer", linecolor="green"];
 a<=b [label="ARM_USBD_SignalEndpointEvent", URL="ARM_USBD_SignalEndpointEvent", linecolor="orange"];
 a=>b [label="ARM_USBD_EndpointTransferGetResult", URL="ARM_USBD_EndpointTransferGetResult", linecolor="green"];
 --- [label="Repeat End"];
 a=>b [label="ARM_USBD_DeviceDisconnect", URL="ARM_USBD_DeviceDisconnect"];
 a=>b [label="ARM_USBD_PowerControl (ARM_POWER_OFF)", URL="ARM_USBD_Initialize"];
 a=>b [label="ARM_USBD_Uninitialize", URL="ARM_USBD_Uninitialize"];
\endmsc
