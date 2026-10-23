---
id: "drv-vstream-vstreamgetblock"
type: "concept"
domain: "drivers"
title: "vStream: vStreamGetBlock"
summary: "This function provides access to the data block used for input or output operations, depending on the streaming direction."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void *vStreamGetBlock (void)
```


This function provides access to the data block used for input or output operations,
depending on the streaming direction.

- For input streams (receiving data): returns a pointer to the oldest unread data block.  
  If no unread block is available, the function returns NULL.

- For output streams (sending data): returns a pointer to the next available empty block where the application can write data.  
  If no empty block is available, the function returns NULL.

The returned block remains valid until it is released using vStreamReleaseBlock.

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
  // ...
  ptrDriver_vStreamAccelerometer->Stop();
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
