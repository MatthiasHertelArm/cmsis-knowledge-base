---
id: "drv-can-interface-can-message-filtering"
type: "concept"
domain: "drivers"
title: "CAN Interface: CAN Message Filtering"
summary: "The CMSIS-Driver for the CAN interface supports ID filtering for the receiving message objects. The receiving CAN node examines the identifier to decide if it was relevant."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Driver for the CAN interface supports ID filtering for the receiving message objects. The receiving CAN node examines the identifier 
to decide if it was relevant. This filtering is done by the CAN peripheral according the settings configured with the function ARM_CAN_ObjectSetFilter.

The function ARM_CAN_ObjectGetCapabilities retrieves the filter capabilities of the CAN message objects stored in ARM_CAN_OBJ_CAPABILITIES.

Data Fields                | CAN Messages Object can be filtered with ...
:--------------------------|:--------------------------------------------
**exact_filtering**        | an exact ID value set by using the function ARM_CAN_ObjectSetFilter with **control** = ARM_CAN_FILTER_ID_EXACT_ADD.
**range_filtering**        | a range ID value set by using the function ARM_CAN_ObjectSetFilter with **control** = ARM_CAN_FILTER_ID_RANGE_ADD.
**mask_filtering**         | a mask ID value set by as using the function ARM_CAN_ObjectSetFilter with **control** = ARM_CAN_FILTER_ID_MASKABLE_ADD.
**multiple_filters**       | ... several filters to capture multiple ID values, or ID value ranges.

**CAN message filtering using an exact ID**

Example: accept in message object #1 only frames with extended ID = 0x1567.
```
  status = ptrCAN->ObjectSetFilter (1, ARM_CAN_FILTER_ID_EXACT_ADD, ARM_CAN_EXTENDED_ID(0x1567), 0);
  if (status != ARM_DRIVER_OK) ... // error handling
```

Example: accept in message object #2 frames with extended ID = 0x3167 and extended ID = 0x42123.
```
  status = ptrCAN->ObjectSetFilter (2, ARM_CAN_FILTER_ID_EXACT_ADD, ARM_CAN_EXTENDED_ID(0x3167), 0);
  if (status != ARM_DRIVER_OK) ... // error handling
  status = ptrCAN->ObjectSetFilter (2, ARM_CAN_FILTER_ID_EXACT_ADD, ARM_CAN_EXTENDED_ID(0x42123), 0);
  if (status != ARM_DRIVER_OK) ... // error handling
```

**CAN message filtering using a range ID**

Example: accept in message object #3 only frames with extended ID >= 0x1567 and extended ID <= 0x1577.
```
  status = ptrCAN->ObjectSetFilter (3, ARM_CAN_FILTER_ID_RANGE_ADD, ARM_CAN_EXTENDED_ID(0x1567), ARM_CAN_EXTENDED_ID(0x1577));
  if (status != ARM_DRIVER_OK) ... // error handling
```


**CAN message filtering using a mask ID**

Using the function ARM_CAN_ObjectSetFilter with **control** = ARM_CAN_FILTER_ID_MASKABLE_ADD allows to specify with **arg** a mask value.
 - if a mask bit is `0`, the corresponding **ID** bit will be accepted, regardless of the value.
 - if a mask bit is `1`, the corresponding **ID** bit will be compared with the value of the ID filter bit; if they match the message will be accepted otherwise the frame is rejected.

Example: accept in message object #0 only frames with extended IDs 0x1560 to 0x156F.
```
  status = ptrCAN->ObjectSetFilter (0, ARM_CAN_FILTER_ID_MASKABLE_ADD, ARM_CAN_EXTENDED_ID(0x1560), 0x1FFFFFF0);
  if (status != ARM_DRIVER_OK) ... // error handling
```

Example: accept in message object #2 only frames with extended IDs 0x35603, 0x35613, 0x35623, and 0x35633.
```
  status = ptrCAN->ObjectSetFilter (2, ARM_CAN_FILTER_ID_MASKABLE_ADD, ARM_CAN_EXTENDED_ID(0x35603), 0x1FFFFFCF);
  if (status != ARM_DRIVER_OK) ... // error handling
```

Example: accept any message in object #4 regardless of the ID.
```
  status = ptrCAN->ObjectSetFilter (4, ARM_CAN_FILTER_ID_MASKABLE_ADD, ARM_CAN_EXTENDED_ID(0), 0);
  if (status != ARM_DRIVER_OK) ... // error handling
```
