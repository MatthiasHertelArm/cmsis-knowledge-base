---
id: "rtos2-thread-management-osthreadprotectprivileged"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadProtectPrivileged"
summary: "The function osThreadProtectPrivileged disables creation of new privileged threads. After its successful execution, no new threads with privilege execution mode (osThreadPrivileged attribute) can be created. Kernel shall be in ready state or running when osThreadProtectPrivileged is called."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadProtectPrivileged (void);
```


The function **osThreadProtectPrivileged** disables creation of new privileged threads. After its successful execution, no new
threads with privilege execution mode (osThreadPrivileged attribute) can be created.
Kernel shall be in ready state or running when **osThreadProtectPrivileged** is called.

Possible osStatus_t return values:
    - **osOK:** the creation of new privileged threads is disabled.
    - **osError:** cannot be executed (kernel not ready).
    - **osErrorISR:** the function **osThreadProtectPrivileged** cannot be called from interrupt service routines.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example:**
```
#include "cmsis_os2.h"
 
int main (void) {
  osStatus_t status;
  :
  status = osKernelInitialize();        // Initialize CMSIS-RTOS2 kernel
  // verify status value here.
  :                                     // Create privileged threads
  status = osThreadProtectPrivileged(); // Disable creation of new privileged threads.
  // verify status value here.
  :                                     // Start the kernel
}
```
