---
id: "rtx-tutorial-configuration"
type: "concept"
domain: "rtos"
title: "tutorial: Configuration"
summary: "So far we have looked at the CMSIS-RTOS2 API. This includes thread management functions, time management and inter-thread communication."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#configuration"
license: "Apache-2.0"
mode: "V"
---

So far we have looked at the CMSIS-RTOS2 API. This includes thread management functions, time management and inter-thread
communication. Now that we have a clear idea of exactly what the RTOS kernel is capable of, we can take a more detailed look
at the configuration file.

RTX_Config.h is the central configuration file for all of the Cortex-M based microcontrollers.  Like the other configuration
files, it is a template file which presents all the necessary configurations as a set of menu options (when viewed in
Configuration Wizard view).

### System Configuration

Before we discuss the settings in the system configuration section, it is worth mentioning what is missing. In earlier
versions of CMSIS-RTOS, it was necessary to define the CPU frequency as part of the RTOS configuration. In CMSIS-RTOS2, the
CPU frequency is now taken from the "SystemCoreClock" variable which is set as part of the CMSIS-Core system startup code.
If you are working with a new microcontroller you will need to check that this value is being set correctly.

As we have seen earlier, we can set the amount of memory allocated to the "Global Dynamic Memory Pool". Next, we can define
the tick frequency in Hertz. This defines the SysTick interrupt rate and is set to 1 ms by default. Generally, I would leave
this frequency at its default setting. However, processor clock speeds are getting ever faster. If you are using a high
performance device you may consider using a faster tick rate.

"Round Robin Thread" switching is also enabled by default in this section. Again, I would recommend leaving these settings
in their default state unless you have a strong requirement to change them. The system configuration settings also allow us
to control the range of messages sent to the event recorder as the RTOS runs.

Finally, if we are setting thread flags from an interrupt they are held in a queue until they are processed. Depending on
your application you may need to increase the size of this queue.

### Thread Configuration

In the Thread Configuration section, we define the basic resources which will be required by the CMSIS-RTOS2 threads. For
each thread we allocate a "default thread stack space" (by default, this is 200 bytes). As you create threads, this memory
will be allocated from the Global Dynamic Mmemory Pool. However, if we enable Object specific memory allocation the RTOS
will define a memory region which is dedicated to thread usage only. If you switch to object specific memory allocation, it
is necessary to provide details about the number and size of threads memory so the RTOS can calculate the maximum memory
requirement.

For object specific memory allocation, we must define the maximum number of user threads (don’t count the idle
or timer threads) which will be running. We must also define the number of threads which have a default stack size and also
the total amount of memory required by threads with custom tack sizes. Once we have defined the memory used by user threads,
we can allocate memory to the idle thread. During development, CMSIS-RTOS can trap stack overflows. When this option is
enabled, an overflow of a thread stack space will cause the RTOS kernel to call the osRtxErrorNotify function which
is located in the RTX_Config.c file. This function gets an error code and then sits in an infinite loop. The stack checking
option is intended for use during debugging and should be disabled on the final application to minimize the kernel overhead.
However, it is possible to modify the osRtxErrorNotify function if enhanced error protection is required in the final
release.

```c
// OS Error Callback function
__WEAK uint32_t osRtxErrorNotify (uint32_t code, void *object_id) {
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
      // Reserved
      break;
  }
  for (;;) {}
//return 0U;
}
```

It is also possible to monitor the maximum stack memory usage during run time. If you check the "Stack Usage Watermark"
option, a pattern (0xCC) is written into each stack space. During runtime, this watermark is used to calculate the maximum
memory usage. In Arm Keil MDK, this figure is reported in the threads section of the View - Watch Window - RTX RTOS window.

This section also allows us to select whether the threads are running in privileged or unprivileged mode. The last option
allows us to define the processor operating mode for the user threads. If you want an easy life, leave this set to
"privileged mode" and you will have full access to all the processor features. However, if you are writing a safety critical
or secure application then "unprivileged mode" can be used to prevent thread access to critical processor registers limiting
run time errors or attempts at intrusion.

### System Timer Configuration

The default timer for use with CMSIS-RTOS is the Cortex-M SysTick timer which is present on nearly all Cortex-M processors.
The input to the SysTick timer will generally be the CPU clock. It is possible to use a different timer by overloading the
kernel timer functions as outlined explained in the CMSIS_RTOS_TickAPI documentation.
