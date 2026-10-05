---
id: "rtos2-kernel-information-and-control-oskernelresume"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelResume"
summary: "CMSIS-RTOS provides extension for tick-less operation which is useful for applications that use extensively low-power modes where the SysTick timer is also disabled."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void osKernelResume (uint32_t sleep_ticks)
```


CMSIS-RTOS provides extension for tick-less operation which is useful for applications that use extensively low-power modes where the SysTick timer is also disabled. 

To provide a time-tick in such power-saving modes a wake-up timer is used to derive timer intervals. The function **osKernelResume** enables the RTOS kernel scheduler and thus wakes up the system from sleep
mode.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
void osRtxIdleThread (void) {
                                               /* The idle thread is running
                                                  when no other thread is ready
                                                  to run.                      */
  unsigned int sleep;
 
  for (;;) {
                                               /* HERE: include optional user
                                                  code to be executed when no
                                                  task runs.                   */
    sleep = osKernelSuspend();                 /* Suspend RTOS kernel scheduler */
 
    if (sleep) {                               /* How long can we sleep?       */
                                               /* "sleep" is in Kernel Timer Ticks
                                                  which is 1ms in this
                                                  configuration                */
       
                                               /* Setup wake-up e.g. watchdog  */
 
      __WFE();                                 /* Enter Power-down mode        */
      
                                               /* After Wake-up                */
      sleep = tc;                              /* Adjust with cycles slept     */  
    }
 
    osKernelResume(sleep);                     /* Resume thread scheduler      */
  }
}
```
