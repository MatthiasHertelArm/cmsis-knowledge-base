---
id: "rtos2-thread-flags"
type: "concept"
domain: "rtos"
title: "Thread Flags"
summary: "Thread Flags are a more specialized version of the Event Flags. See CMSIS_RTOS_EventFlags. While Event Flags can be used to globally signal a number of threads, thread flags are only sent to a single specific thread."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
license: "Apache-2.0"
mode: "V"
---

Synchronize threads using flags.

Thread Flags are a more specialized version of the Event Flags. See CMSIS_RTOS_EventFlags.
While Event Flags can be used to globally signal a number of threads, thread flags are only sent to a single specific thread.
Every thread instance can receive thread flags without any additional allocation of a thread flags object.

**Note:** Thread flag management functions cannot be called from Interrupt Service Routines, except
for osThreadFlagsSet.

**Usage Example**

The following (incomplete) code excerpt sketches the usage principals for **Thread Flags**.

The behavior is the following:
-	app_main starts executing
-	statement A sets thread flags to 0x02 (flags = 0x02 – after set)
-	app_main enters delay
-	execution switches to threadX
-	statement B waits for flag 0x01 and blocks since flag is not set
-	execution switches to app_main
-	statement C sets thread flags to 0x07
-	threadX wakes-up and clears flag 0x01, thread flags = 0x06, return value set to 0x07 (before clear), note: all this happens during statement C
-	statement C returns with flags = 0x06
-	app_main enters delay
-	execution switches to threadX
-	statement B returns with flagsX = 0x07
 
```
#include "cmsis_os2.h"
 
osThreadId_t tid;
uint32_t     flagsX;
uint32_t     flags;
 
void threadX (void *argument) {
  
  osDelay(1U);
  for (;;) {
    flagsX = osThreadFlagsWait(0x0001U, osFlagsWaitAny, osWaitForever); /* B */
  }
}
 
void app_main (void *argument) {
 
  tid = osThreadNew(threadX, NULL, NULL);
 
  flags = osThreadFlagsSet(tid, 0x0002U); /* A */
  osDelay(2U);
  flags = osThreadFlagsSet(tid, 0x0005U); /* C */
  osDelay(2U);
 
  for(;;);
}
```
