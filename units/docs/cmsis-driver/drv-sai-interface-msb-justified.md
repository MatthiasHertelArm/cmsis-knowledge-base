---
id: "drv-sai-interface-msb-justified"
type: "concept"
domain: "drivers"
title: "SAI Interface: MSB Justified"
summary: "Unlike I2S, in MSB Justified the word select (WS) signals the left channel when it is active high and the right channel, when it is active low. The signal changes when the first actual SD data is available."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

**MSB** **Justified** is much like Driver_SAI_I2S, with a few differences:



Unlike I2S, in MSB Justified the word select (**WS)** signals the left channel when it is active high and the right channel,
when it is active low. The signal changes when the first actual **SD** data is available. It might happen that a frame (left
or right) is not fully filled with data. In this case, all data after the LSB is forced to zero.

In terms of the CMSIS-Driver for SAI, the MSB Justified protocol can be described as follows:
- Data Size: 8..32 (MSB first)
- Clock Polarity: Drive on falling edge, Capture on rising edge
- Frame Length: 2 * Slot Size
- Frame Sync Width: Frame Length / 2
- Frame Sync Polarity: Active High
- Slot Count: 2 (L R)
- Slot Size: Data Size or higher (16/32)
- Slot Offset: 0 (Zero padding after Data: Slot Size - Data Size)
