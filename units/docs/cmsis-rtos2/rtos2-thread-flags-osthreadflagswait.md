---
id: "rtos2-thread-flags-osthreadflagswait"
type: "concept"
domain: "rtos"
title: "Thread Flags: osThreadFlagsWait"
summary: "The function osThreadFlagsWait suspends the execution of the currently RUNNING thread until any or all of the thread flags specified with the parameter flags are set. When these thread flags are already set, the function returns instantly."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadFlagsWait (uint32_t flags, uint32_t options, uint32_t timeout)
```

The function **osThreadFlagsWait** suspends the execution of the currently RUNNING thread until any or all of the thread
flags specified with the parameter _flags_ are set. When these thread flags are already set, the function returns instantly.
Otherwise the thread is put into the state BLOCKED.

The parameter **options** specifies the wait condition:
|Option              |                                                       |
|--------------------|-------------------------------------------------------|
|**osFlagsWaitAny**   |   Wait for any flag (default).                        |
|**osFlagsWaitAll**   |   Wait for all flags.                                 |
|**osFlagsNoClear**   |   Do not clear flags which have been specified to wait for.  |

If `osFlagsNoClear` is set in the options osThreadFlagsClear can be used to clear flags manually.
Otherwise **osThreadFlagsWait** automatically clears the flags waited for.

The parameter timeout represents a number of timer ticks and is an upper bound. The
exact time delay depends on the actual time elapsed since the last timer tick. 

The function returns the flags before clearing, or an error code if highest bit is set (refer to flags_error_codes).

Possible flags_error_codes return values:
    - **osFlagsErrorUnknown:** unspecified error, i.e. not called from a running threads context.
    - **osFlagsErrorTimeout:** awaited flags have not been set in the given time.
    - **osFlagsErrorResource:** awaited flags have not been set when no _timeout_ was specified.
    - **osFlagsErrorParameter:** Parameter **flags** has highest bit set.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread (void* arg) {
  ;
  osThreadFlagsWait(0x00000001U, osFlagsWaitAny, osWaitForever); // Wait forever until thread flag 1 is set.
  ;
  osThreadFlagsWait(0x00000003U, osFlagsWaitAny, osWaitForever); // Wait forever until either thread flag 0 or 1 is set.
  ;
  osThreadFlagsWait(0x00000003U, osFlagsWaitAll, 10U); // Wait for 10 timer ticks until thread flags 0 and 1 are set. Timeout afterwards.
  ;
  osThreadFlagsWait(0x00000003U, osFlagsWaitAll | osFlagsNoClear, osWaitForever); // Same as the above, but the flags will not be cleared.
}
```
