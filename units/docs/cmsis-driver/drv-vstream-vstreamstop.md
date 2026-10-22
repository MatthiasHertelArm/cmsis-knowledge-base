---
id: "drv-vstream-vstreamstop"
type: "concept"
domain: "drivers"
title: "vStream: vStreamStop"
summary: "This function stops the ongoing streaming process initiated by vStreamStart and resets the stream, by discarding any remaining or incomplete data blocks."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t vStreamStop (void)
```


This function stops the ongoing streaming process initiated by vStreamStart and resets the
stream, by discarding any remaining or incomplete data blocks.

Calling this function halts data transfers and prepares the stream for either shutdown or restart.
After stopping, the stream can be restarted using vStreamStart without requiring re-initialization or reconfiguration, provided the buffer settings remain valid.

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
  ptrDriver_vStreamAccelerometer->Stop();
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
