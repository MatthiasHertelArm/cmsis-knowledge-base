---
id: "drv-can-interface-can-message-objects"
type: "concept"
domain: "drivers"
title: "CAN Interface: CAN Message Objects"
summary: "The CMSIS-Driver for the CAN interface provides multiple CAN message objects, which can be seen as individual communication channels. The number of available CAN message objects depends on the CAN peripheral."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Driver for the CAN interface provides multiple CAN message objects, which can be seen as individual communication channels.
The number of available CAN message objects depends on the CAN peripheral. The function ARM_CAN_GetCapabilities returns 
the maximum number of available CAN message objects. The number is encoded in the structure ARM_CAN_CAPABILITIES in the data field **num_objects.**
CAN message objects are addressed with the functions listed below, whereby the parameter **obj_idx** addresses an individual object.
The valid range for **obj_idx** is `[0 .. (**num_objects** - 1)]`.

Function                           | Description
:----------------------------------|:--------------------------------------------
ARM_CAN_ObjectGetCapabilities | Retrieves message object capabilities such as receive, transmit, Remote_Frame automatic handling and can_filtering.
ARM_CAN_ObjectSetFilter       | Allows to set-up CAN ID filtering for the message object.
ARM_CAN_ObjectConfigure       | Allows to configure the message object for receive, transmit or Remote_Frame automatic handling.
ARM_CAN_MessageRead           | Read received message from the message object.
ARM_CAN_MessageSend           | Send CAN message or send Remote_Frame or set CAN message to be sent automatically on reception of matching Remote_Frame on the message object.
ARM_CAN_SignalObjectEvent     | Callback function that signals a message transfer or a received message overrun.

Each CAN message object may have different capabilities. Before using a CAN message object, call the 
function ARM_CAN_ObjectGetCapabilities to verify the available features.
