---
id: "rtx-cmsis-rtos2-api-osrtxerrornotify"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorNotify"
summary: "Some system error conditions can be detected during runtime. If the RTX kernel detects a runtime error, it calls the runtime error function osRtxErrorNotify for an object specified by parameter object_id."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osRtxErrorNotify (uint32_t code, void *object_id);
```

- `code` (in): The code to identify the error condition.
- `object_id` (in): A reference to any RTX object to identify the object that caused the issue, can be `NULL`.
Returns: 0 (reserved for future implementations)

Some system error conditions can be detected during runtime. If the RTX kernel detects a runtime error, it calls the runtime
error function **osRtxErrorNotify** for an object specified by parameter _object_id._

The parameter _code_ passes the actual error code to this function:
| Error Code                        | Description                                                                       |
|-----------------------------------|-----------------------------------------------------------------------------------|
| osRtxErrorStackOverflow      | Stack overflow detected for thread (thread_id=object_id)                          |
| osRtxErrorISRQueueOverflow   | ISR Queue overflow detected when inserting object (object_id)                     |
| osRtxErrorTimerQueueOverflow | User Timer Callback Queue overflow detected for timer (timer_id=object_id)        |
| osRtxErrorClibSpace          | Standard C/C++ library libspace not available: increase `OS_THREAD_LIBSPACE_NUM` |
| osRtxErrorClibMutex          | Standard C/C++ library mutex initialization failed                                |
| osRtxErrorSVC                | Invalid SVC function called (function=object_id)                                  |

The function **osRtxErrorNotify** must contain an infinite loop to prevent further program execution. You can use an emulator
to step over the infinite loop and trace into the code introducing a runtime error. For the overflow errors this means you
need to increase the size of the object causing an overflow.

**Code Example**
```
#include "rtx_os.h"
 
uint32_t osRtxErrorNotify (uint32_t code, void *object_id) {
  (void)object_id;
 
  switch (code) {
    case osRtxErrorStackOverflow:
      // Stack overflow detected for thread (thread_id=object_id)
      break;
    case osRtxErrorISRQueueOverflow:
      // ISR Queue overflow detected when inserting object (object_id)
      break;
    case osRtxErrorTimerQueueOverflow:
      // User Timer Callback Queue overflow detected for timer (timer_id=object_id)
      break;
    case osRtxErrorClibSpace:
      // Standard C/C++ library libspace not available: increase OS_THREAD_LIBSPACE_NUM
      break;
    case osRtxErrorClibMutex:
      // Standard C/C++ library mutex initialization failed
      break;
    case osRtxErrorSVC:
      // Invalid SVC function called (function=object_id)
      break;
    default:
      break;
  }
  for (;;) {}
//return 0U;
}
```
