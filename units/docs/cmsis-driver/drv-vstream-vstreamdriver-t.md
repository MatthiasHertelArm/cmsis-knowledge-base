---
id: "drv-vstream-vstreamdriver-t"
type: "concept"
domain: "drivers"
title: "vStream: vStreamDriver_t"
summary: "This structure provides function pointers to access the vStream driver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
vStreamDriver_t
```


This structure provides function pointers to access the vStream driver.

Recommended naming convention for access structures:
  - Driver_vStream<Device>
  - Examples:
    - Driver_vStreamAccelerometer
    - Driver_vStreamGyroscope
    - Driver_vStreamHumidity
    - Driver_vStreamTemperature
    - Driver_vStreamIMU
    - Driver_vStreamAudioIn
    - Driver_vStreamAudioOut
    - Driver_vStreamVideoIn
    - Driver_vStreamVideoOut

****************************************************************************************************************
