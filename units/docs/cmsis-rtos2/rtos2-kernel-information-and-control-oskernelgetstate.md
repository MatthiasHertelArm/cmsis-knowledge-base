---
id: "rtos2-kernel-information-and-control-oskernelgetstate"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelGetState"
summary: "The function osKernelGetState returns the current state of the kernel and can be safely called before the RTOS is initialized or started (call to osKernelInitialize or osKernelStart)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osKernelState_t osKernelGetState (void)
```


The function **osKernelGetState** returns the current state of the kernel and can be safely called before the RTOS is
initialized or started (call to osKernelInitialize or osKernelStart). In case it fails it will return `osKernelError,`
otherwise it returns the kernel state (refer to osKernelState_t for the list of kernel states).

Possible osKernelState_t return values:
- osKernelError if an unspecific error occurred.
- the actual kernel state otherwise.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**
```
int main (void) {
  // System Initialization
  SystemCoreClockUpdate();
  // ...
  if(osKernelGetState() == osKernelInactive) {     // Is the kernel initialized?
     osKernelInitialize();                         // Initialize CMSIS-RTOS kernel
  }
  ;
}
```
