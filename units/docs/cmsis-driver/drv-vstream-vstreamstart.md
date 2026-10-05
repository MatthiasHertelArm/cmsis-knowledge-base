---
id: "drv-vstream-vstreamstart"
type: "concept"
domain: "drivers"
title: "vStream: vStreamStart"
summary: "This function initiates the streaming operation based on the specified mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vStreamStart (uint32_t mode)
```


This function initiates the streaming operation based on the specified mode.

Before calling **vStreamStart:**
  - The interface must be initialized using vStreamInitialize.
  - A valid buffer must be configured using vStreamSetBuf.

The **mode** parameter defines the streaming behavior:
  - VSTREAM_MODE_CONTINUOUS : Streaming continues until explicitly stopped.
  - VSTREAM_MODE_SINGLE : Streaming stops automatically after transferring a single data block.

**Code Example**:
```
#include "cmsis_vstream.h"

// vStream driver
extern vStreamDriver_t     Driver_vStreamAccelerometer;
static vStreamDriver_t *ptrDriver_vStreamAccelerometer = &Driver_vStreamAccelerometer;

static uint32_t vstream_buf[256];

int main (void) {

  SystemCoreClockUpdate();              // System Initialization

  ptrDriver_vStreamAccelerometer->Initialize(NULL);
  ptrDriver_vStreamAccelerometer->SetBuf(vstream_buf, sizeof(vstream_buf), sizeof(vstream_buf)/2);
  ptrDriver_vStreamAccelerometer->Start(VSTREAM_MODE_CONTINUOUS);
  // ...
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
