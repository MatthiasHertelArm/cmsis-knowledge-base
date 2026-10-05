---
id: "drv-sai-interface-lsb-justified"
type: "concept"
domain: "drivers"
title: "SAI Interface: LSB Justified"
summary: "In terms of the CMSIS-Driver for SAI, the LSB Justified protocol can be described as follows: - Data Size: 8..32 (MSB first) - Clock Polarity: Drive on falling edge, Capture on rising edge - Frame Length: 2Slot Size …"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

**LSB** **Justified** is much like Driver_SAI_MSB, with the single difference that the padding 0's are sent before the
first actual data (MSB on **SD):**



In terms of the CMSIS-Driver for SAI, the LSB Justified protocol can be described as follows:
- Data Size: 8..32 (MSB first)
- Clock Polarity: Drive on falling edge, Capture on rising edge
- Frame Length: 2*Slot Size
- Frame Sync Width: Frame Length / 2
- Frame Sync Polarity: Active High
- Slot Count: 2
- Slot Size: Data Size or higher (16/32)
- Slot Offset: Slot Size - Data Size (Zero padding before Data: Slot Size - Data Size)
