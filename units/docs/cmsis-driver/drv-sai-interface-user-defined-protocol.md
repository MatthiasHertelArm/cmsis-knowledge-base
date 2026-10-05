---
id: "drv-sai-interface-user-defined-protocol"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol"
summary: "Using the control structs of the CMSIS-Driver SAI, it is possible to create support for nearly all serial audio protocols that are available today."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

Using the control structs of the CMSIS-Driver SAI, it is possible to create support for nearly all serial audio protocols
that are available today. 



The following properties can be configured for a user protocol:
- Data Size in bits (8..32)
- Data Bit Order: MSB first (default) or LSB first
- Clock Polarity:
  - Driver on falling edge, Capture on rising edge (default)
  - Driver on rising edge, Capture on falling edge
- Frame Length in bits
- Frame Sync Width in bits (default=1)
- Frame Sync Polarity: active high (default) or low
- Frame Sync Early: Sync signal one bit before the first bit of frame
- Slot Count: number of slots in frame (default=1)
- Slot Size: equal to data size (default) or 16 or 32-bit
- Slot Offset: offset of first data bit in slot (default=0)

For more information, refer to ARM_SAI_Control that explains the different configuration options in more detail.
