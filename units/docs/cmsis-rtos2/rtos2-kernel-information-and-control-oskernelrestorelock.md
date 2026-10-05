---
id: "rtos2-kernel-information-and-control-oskernelrestorelock"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelRestoreLock"
summary: "The function osKernelRestoreLock restores the previous lock state after osKernelLock or osKernelUnlock."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t osKernelRestoreLock (int32_t lock)
```


The function **osKernelRestoreLock** restores the previous lock state after osKernelLock or osKernelUnlock.

The argument _lock_ specifies the lock state as obtained by osKernelLock or osKernelUnlock.

The function returns the new value of the lock state (`1` if it was locked, `0` if it was unlocked), or a
negative number representing an error code otherwise (refer to osStatus_t).

Possible osStatus_t return values:
- **osError** if an unspecific error occurred.
- **osErrorISR** if called from interrupt other than fault or osWatchdogAlarm_Handler.
- **osErrorSafetyClass** if the calling thread safety class is lower than the kernel protect safety class.

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
