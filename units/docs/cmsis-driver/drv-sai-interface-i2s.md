---
id: "drv-sai-interface-i2s"
type: "concept"
domain: "drivers"
title: "SAI Interface: I2S"
summary: "Integrated Interchip Sound (I2S) is a serial bus interface that connects digital audio devices together. It was introduced by Philips (now NXP) in the late 80's and last revised 1996."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

Integrated Interchip Sound (**I2S)** is a serial bus
interface that connects digital audio devices together. It was introduced by Philips (now
NXP) in the late 80's and last revised 1996. It uses pulse code modulation
to exchange the audio data between the devices. The following timing diagram explains the operation:
 


I2S separates the clock (**SCK)** from the serial data (**SD),** resulting in a lower jitter. A complete audio data frame
consists of two slots, one for the left channel and one for the right. The slot size equals the data size.
The word select (**WS)** line lets the device know whether the left channel (WS is low) or the right channel (WS is high) is
currently being transmitted. WS has a 50% duty-cycle signal that has the same frequency as the sample frequency. It is an
early signal, meaning that the WS line changes one clock cycle before the actual data (SD) is transmitted (left or right).
The data on SD is always transmitted MSB first and can have a data size of 8 up to 32 bits.

In terms of the CMSIS-Driver for SAI, the I2S protocol can be described as follows:
- Data Size: 8..32 (MSB first)
- Clock Polarity: Drive on falling edge, Capture on rising edge
- Frame Length: 2 * Data Size = 2 * Slot Size
- Frame Sync Width: Frame Length / 2
- Frame Sync Polarity: Active Low
- Frame Sync Early
- Slot Count: 2 (L R)
- Slot Size: Data Size
- Slot Offset: 0
