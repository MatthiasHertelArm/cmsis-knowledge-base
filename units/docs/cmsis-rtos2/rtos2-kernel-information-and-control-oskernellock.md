---
id: "rtos2-kernel-information-and-control-oskernellock"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelLock"
summary: "The function osKernelLock allows to lock all task switches. It returns the previous value of the lock state (1 if it was locked, 0 if it was unlocked), or a negative number representing an error code otherwise (refer to osStatus_t)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t osKernelLock (void)
```


The function **osKernelLock** allows to lock all task switches. It returns the previous value of the lock state (`1` if
it was locked, `0` if it was unlocked), or a negative number representing an error code otherwise (refer to
osStatus_t).

Possible osStatus_t return values:
- **osError** if an unspecific error occurred.
- **osErrorISR** if called from an Interrupt Service Routine.
- **osErrorSafetyClass** if the calling thread safety class is lower than the kernel protect safety class.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
  int32_t state = osKernelLock();
  // ... critical code
  osKernelRestore(state);
```
