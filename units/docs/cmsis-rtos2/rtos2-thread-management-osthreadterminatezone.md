---
id: "rtos2-thread-management-osthreadterminatezone"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadTerminateZone"
summary: "The function osThreadTerminateZone terminates execution of threads assigned to the MPU Protected Zone as given by zone parameter."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadTerminateZone (uint32_t zone);
```


The function **osThreadTerminateZone** terminates execution of threads assigned to the MPU Protected Zone as given by _zone_ parameter.

Possible osStatus_t return values:
    - **osOK:** the threads within the specified MPU Protected Zone have been terminated successfully.
    - **osErrorParameter:** _zone_ is invalid.
    - **osErrorResource:** no other READY thread exists.
    - **osErrorISR:** the function **osThreadTerminateZone** is called from interrupt other than fault.
    - **osError:** the function **osThreadTerminateZone** is called from thread.

**Note:** **osThreadTerminateZone** destroys non-joinable threads and removes their thread IDs from the system. Subsequent access to a terminated thread via its thread ID (for example osThreadGetState) will return an osThreadError. Joinable threads will not be destroyed and return the status osThreadTerminated until they are joined with osThreadJoin.

**Code Example:**
```
#include "cmsis_os2.h"
 
void TerminateFaultedThreads (void) {  // to be called from an exception fault context
  osStatus_t status;
 
  status = osThreadTerminateZone(3U); // Terminates threads assigned to MPU Protected Zone 3
  // verify status value here.
}
```
