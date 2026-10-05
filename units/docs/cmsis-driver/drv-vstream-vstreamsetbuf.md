---
id: "drv-vstream-vstreamsetbuf"
type: "concept"
domain: "drivers"
title: "vStream: vStreamSetBuf"
summary: "This function registers a memory buffer for use by the Virtual Streaming driver. The buffer is used for reading or writing fixed-size data blocks, depending on the streaming direction."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vStreamSetBuf (void *buf, uint32_t buf_size, uint32_t block_size)
```


This function registers a memory buffer for use by the Virtual Streaming driver.  
The buffer is used for reading or writing fixed-size data blocks, depending on the streaming direction.

Memory buffer recommendations:
  - the buffer should be aligned to a 4-byte boundary, to facilitate DMA usage.
  - **buf_size** should be an integer multiple of **block_size,** otherwise the largest multiple that fits will be used.
  - a minimum of two blocks is recommended to ensure proper buffering and streaming continuity.

If **block_size** is larger than **buf_size,** the function returns VSTREAM_ERROR_PARAMETER.

This function must be called after initialization and before starting the stream.

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
  // ...
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
