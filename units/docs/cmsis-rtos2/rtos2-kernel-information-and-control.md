---
id: "rtos2-kernel-information-and-control"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control"
summary: "Provides version/system information and starts/controls the RTOS Kernel."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

Provides version/system information and starts/controls the RTOS Kernel.
 
The kernel Information and Control function group allows to:
  - obtain information about the system and the underlying kernel.
  - obtain version information about the CMSIS-RTOS API.
  - initialize of the RTOS kernel for creating objects.
  - start the RTOS kernel and thread switching.
  - check the execution status of the RTOS kernel.

**Note:** The kernel information and control functions cannot be called from
Interrupt Service Routines.
**Note:** The kernel initialization is documented in SystemStartup.

**Code Example**
```
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
