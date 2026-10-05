---
id: "rtos2-kernel-information-and-control-oskernelstart"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelStart"
summary: "The function osKernelStart starts the RTOS kernel and begins thread switching. It will not return to its calling function in case of success."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osKernelStart (void)
```


The function **osKernelStart** starts the RTOS kernel and begins thread switching. It will not return to its calling function
in case of success. Before it is successfully executed, only the functions osKernelGetInfo, osKernelGetState, and
object creation functions (**osXxxNew)** may be called.

At least one initial thread should be created prior osKernelStart, see osThreadNew.

Possible osStatus_t return values:
- **osError** if an unspecific error occurred.
- **osErrorISR** if called from an Interrupt Service Routine.
 
**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
int main (void) {
  // System Initialization
  SystemCoreClockUpdate();
  // ...
  if(osKernelGetState() == osKernelInactive) {
    osKernelInitialize();
  }
  ; // ... Start Threads
  if (osKernelGetState() == osKernelReady) {        // If kernel is ready to run...
    osKernelStart();                                // ... start thread execution
    }
  
  while(1);                                         // only reached in case of error
}
```
