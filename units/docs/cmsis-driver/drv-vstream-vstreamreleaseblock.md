---
id: "drv-vstream-vstreamreleaseblock"
type: "concept"
domain: "drivers"
title: "vStream: vStreamReleaseBlock"
summary: "This function finalizes the use of the data block returned by vStreamGetBlock."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vStreamReleaseBlock (void)
```


This function finalizes the use of the data block returned by vStreamGetBlock.

- For input streams: marks the block as processed, making it available for reuse by the driver.
- For output streams: commits the block for transmission, indicating that the data is ready to be streamed out.

This function must be called after processing or preparing the data block returned by vStreamGetBlock to maintain proper buffer flow and avoid data loss or stalling.

**Code Example**:
```
#include "cmsis_vstream.h"

// vStream driver
extern vStreamDriver_t     Driver_vStreamAccelerometer;
static vStreamDriver_t *ptrDriver_vStreamAccelerometer = &Driver_vStreamAccelerometer;

static uint32_t vstream_buf[256];

int main (void) {
  static volatile uint32_t *ptr_sensor_data_block;

  SystemCoreClockUpdate();              // System Initialization

  ptrDriver_vStreamAccelerometer->Initialize(NULL);
  ptrDriver_vStreamAccelerometer->SetBuf(vstream_buf, sizeof(vstream_buf), sizeof(vstream_buf)/2);
  ptrDriver_vStreamAccelerometer->Start(VSTREAM_MODE_CONTINUOUS);
  do {
    ptr_sensor_data_block = ptrDriver_vStreamAccelerometer->GetBlock();
  } while (ptr_sensor_data_block == NULL);
  // Do something with sensor data
  // ...
  ptrDriver_vStreamAccelerometer->ReleaseBlock();
  ptrDriver_vStreamAccelerometer->Stop();
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
