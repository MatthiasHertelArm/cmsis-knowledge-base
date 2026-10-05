---
id: "rtos2-kernel-information-and-control-oskernelunlock"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelUnlock"
summary: "The function osKernelUnlock resumes from osKernelLock. It returns the previous value of the lock state (1 if it was locked, 0 if it was unlocked), or a negative number representing an error code otherwise (refer to osStatust)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t osKernelUnlock (void)
```


The function **osKernelUnlock** resumes from osKernelLock. It returns the previous value of the lock state (`1` if
it was locked, `0` if it was unlocked), or a negative number representing an error code otherwise (refer to
osStatus_t).

Possible osStatus_t return values:
- **osError** if an unspecific error occurred.
- **osErrorISR** if called from an Interrupt Service Routine.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
  int32_t sl = osKernelLock();
  // ... critical code
  {
    int32_t su = osKernelUnlock();
    // ... uncritical code
    osKernelRestoreLock(su);
  }
  // ... critical code
  osKernelRestoreLock(sl);
```
