---
id: "drv-sai-interface-pcm"
type: "concept"
domain: "drivers"
title: "SAI Interface: PCM"
summary: "Pulse Code Modulation (PCM) differs to the previous protocols in a few ways:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

Pulse Code Modulation (**PCM)** differs to
the previous protocols in a few ways:



- Only one channel is transferred.

- There are two types of synchronization modes available:
  - In **short** **frame** sync mode, the falling edge of **Frame** **Sync** indicates the start of the serial data **SD.** **Frame** **Sync** is always
    one clock cycle long.
  - In **long** **frame** sync mode, the rising edge of **Frame** **Sync** indicates the start of the serial data **SD.** **Frame** **Sync** stays active
    high for 13 clock cycles.

In terms of the CMSIS-Driver for SAI, the PCM protocol can be described as follows:\n
**PCM** **Short** **Frame**
- Data Size: 8..32 (MSB first)
- Clock Polarity: Drive on falling edge, Capture on rising edge
- Frame Length: Slot Size
- Frame Sync Width: 1
- Frame Sync Polarity: Active High
- Frame Sync Early
- Slot Count: 1
- Slot Size: Data Size or higher (16/32)
- Slot Offset: 0

**PCM** **Long** **Frame**
- Data Size: 16..32 (MSB first)
- Clock Polarity: Drive on falling edge, Capture on rising edge
- Frame Length: Slot Size
- Frame Sync Width: 13
- Frame Sync Polarity: Active High
- Slot Count: 1
- Slot Size: Data Size or higher (32)
- Slot Offset: 0
