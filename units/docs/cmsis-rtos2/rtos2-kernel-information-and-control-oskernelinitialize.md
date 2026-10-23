---
id: "rtos2-kernel-information-and-control-oskernelinitialize"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelInitialize"
summary: "The function osKernelInitialize initializes the RTOS Kernel. Before it is successfully executed, only the functions osKernelGetInfo and osKernelGetState may be called."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osKernelInitialize (void)
```


The function **osKernelInitialize** initializes the RTOS Kernel. Before it is successfully executed, only the functions
osKernelGetInfo and osKernelGetState may be called.
 
Possible osStatus_t return values:
- **osOK** in case of success.
- **osError** if an unspecific error occurred.
- **osErrorISR** if called from an Interrupt Service Routine.
- **osErrorNoMemory** if no memory could be reserved for the operation.

**Note:** This function **cannot** be called from Interrupt Service Routines.

** Code Example**
```
#include "RTE_Components.h"
#include  CMSIS_device_header
#include "cmsis_os2.h"
 
/*----------------------------------------------------------------------------
Application main thread
---------------------------------------------------------------------------*/
void app_main (void *argument) {
 
  // ...
  for (;;) {}
}
 
int main (void) {
 
  // System Initialization
  SystemCoreClockUpdate();
  // ...
 
  osKernelInitialize();                 // Initialize CMSIS-RTOS
  osThreadNew(app_main, NULL, NULL);    // Create application main thread
  osKernelStart();                      // Start thread execution
  for (;;) {}
}
```
