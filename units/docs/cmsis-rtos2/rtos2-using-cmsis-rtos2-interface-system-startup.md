---
id: "rtos2-using-cmsis-rtos2-interface-system-startup"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: System Startup"
summary: "When program execution reaches main() function there is a recommended order to initialize the hardware and start the kernel."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#system-startup"
license: "Apache-2.0"
mode: "V"
---

When program execution reaches `main()` function there is a recommended order to initialize the hardware and start the kernel.

Your application's `main()` should implement at least the following in the given order:

 1. Initialize and configure hardware including peripherals, memory, pins, clocks and the interrupt system.
 2. Update the system core clock using the respective [CMSIS-Core (Cortex-M)](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../Core/group__system__init__gr.html) \if ARMCA or [CMSIS-Core (Cortex-A)](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../Core_A/group__system__init__gr.html) \endif function.
 3. Initialize the RTOS kernel using osKernelInitialize.
 4. Optionally, create one thread (for example `app_main`) using osThreadNew, which will be used as a main thread . This thread should take care of creating and starting objects, once it is run by the scheduler. Alternatively, threads can be created directly in `main()`.
 5. Start the RTOS scheduler using osKernelStart which also configures the system tick timer and initializes RTOS specific interrupts. This function does not return in case of successful execution. Therefore, any application code after `osKernelStart` will not be executed.

> **Note**
> - Modifying priorities and groupings in the NVIC by the application after the above sequence is not recommended.
> - Before executing osKernelStart, only the functions osKernelGetInfo, osKernelGetState, and object creation functions (osXxxNew) may be called.

**Code Example**

```c
/*----------------------------------------------------------------------------
 * CMSIS-RTOS 'main' function template
 *---------------------------------------------------------------------------*/
 
#include "RTE_Components.h"
#include  CMSIS_device_header
#include "cmsis_os2.h"
 
/*----------------------------------------------------------------------------
 * Application main thread
 *---------------------------------------------------------------------------*/
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
