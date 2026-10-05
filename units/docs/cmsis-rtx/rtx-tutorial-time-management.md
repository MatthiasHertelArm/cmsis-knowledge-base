---
id: "rtx-tutorial-time-management"
type: "concept"
domain: "rtos"
title: "tutorial: Time Management"
summary: "As well as running your application code as threads, the RTOS also provides some timing services which can be accessed through RTOS system calls."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#time-management"
license: "Apache-2.0"
mode: "V"
---

As well as running your application code as threads, the RTOS also provides some timing services which can be accessed through RTOS system calls.

### Time Delay

The most basic of these timing services is a simple timer delay function. This is an easy way of providing timing delays
within your application. Although the RTOS kernel size is quoted as 5 KB, features such as delay loops and simple scheduling
loops are often part of a non-RTOS application and would consume code bytes anyway, so the overhead of the RTOS can be less
than it immediately appears.

```c
void osDelay (uint32_t ticks)
```

This call will place the calling thread into the WAIT_DELAY state for the specified number of milliseconds. The scheduler
will pass execution to the next thread in the READY state.

When the timer expires, the thread will leave the WAIT_DELAY  state and move to the READY state. The thread will resume
running when the scheduler moves it to the RUNNING state. If the thread then continues executing without any further
blocking OS calls, it will be descheduled at the end of its time slice and be placed in the ready state, assuming another
thread of the same priority is ready to run.

### Absolute Time Delay

In addition to the osDelay function which gives a relative time delay starting from the instant it is called, there
is also a delay function which halts a thread until a specific point in time:

```c
osStatus osDelayUntil (uint32_t ticks)
```

The osDelayUntil function will halt a thread until a specific value of kernel timer ticks is reached. There are a
number of kernel functions that allow you to read both the current SysTick count and the kernel ticks count.

| Kernel timer functions |
|------------------------|
| uint64_t osKernelGetTickCount(void)     |
| uint32_t osKernelGetTickFreq(void)      |
| uint32_t osKernelGetSysTimerCount(void) |
| uint32_t osKernelGetSysTimerFreq(void)  |

### Exercise 6 - Time Management

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 06 Time Management** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

### Virtual Timers

The CMSIS-RTOS API can be used to define any number of virtual timers which act as count down timers. When they expire, they
will run a user call-back function to perform a specific action. Each timer can be configured as a one shot or repeat timer.
A virtual timer is created by first defining a timer structure:

```c
static const struct osTimerAttr_t timerAttr_timer0 = {
  const char* name;      ///< name of the timer
  uint32_t    attr_bits; ///< attribute bits
  void*       cb_mem;    ///< memory for control block
  uint32_t    cb_size;   ///< size of provided memory for control block
}
```

This defines a name for the timer. The timer must then be instantiated by an RTOS
thread providing a pointer to the callback function and its parameter.:

```c
osTimerId_t timer0_handle;
timer0_handle = osTimerNew(&callback, osTimerPeriodic,(void *)<parameter>, &timerAttr_timer0);
```

This creates the timer and defines it as a periodic timer or a single shot timer (osTimerOnce). The next parameter
passes an argument to the call back function when the timer expires:

```c
osTimerStart (timer0_handle,0x100);
```

The timer can then be started at any point in a thread the timer start function invokes the timer by its handle and defines
a count period in kernel ticks.

### Exercise 7 - Virtual Timer

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 07 Virtual Timers** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

### Idle Thread

The final timer service provided by the RTOS isn't really a timer, but this is probably the best place to discuss it. If
during our RTOS program we have no thread running and no thread ready to run (e.g. they are all waiting on delay functions),
then the RTOS will start to run the Idle Thread. This thread is automatically created when the RTOS starts and runs at the
lowest priority. The Idle Thread function is located in the RTX_Config.c file:

```c
__WEAK __NO_RETURN void osRtxIdleThread (void *argument) {
  (void)argument;
 
  for (;;) {}
}
```

You can add any code to this thread, but it has to obey the same rules as user threads. The simplest use of the idle demon
is to place the microcontroller into a low-power mode when it is not doing anything.

```c
__WEAK __NO_RETURN void osRtxIdleThread (void *argument) {
  (void)argument;
 
  for (;;) {
    __WFE();
  }
}
```

What happens next depends on the power mode selected in the microcontroller. At a minimum, the CPU will halt until an
interrupt is generated by the SysTick timer and execution of the scheduler will resume. If there is a thread ready to run,
then execution of the application code will resume. Otherwise, the idle demon will be reentered and the system will go back
to sleep.

### Exercise 8 - Idle Thread

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 08 Idle Thread** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
