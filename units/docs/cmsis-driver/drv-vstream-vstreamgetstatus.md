---
id: "drv-vstream-vstreamgetstatus"
type: "concept"
domain: "drivers"
title: "vStream: vStreamGetStatus"
summary: "This function returns the current operational status of the Virtual Streaming interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
vStreamStatus_t vStreamGetStatus (void)
```


This function returns the current operational status of the Virtual Streaming interface.

The returned structure includes the following information:
  - Streaming activity status.
  - Overflow or underflow conditions.
  - End-of-stream (EOS) indication.

Use this function to monitor the health and state of the streaming process during runtime.

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
  if (ptrDriver_vStreamAccelerometer->GetStatus().active == 0U) {
    // If streaming is not active exit
  }
  // ...
  ptrDriver_vStreamAccelerometer->Stop();
  ptrDriver_vStreamAccelerometer->Uninitialize();
}
```

*******************************************************************************
