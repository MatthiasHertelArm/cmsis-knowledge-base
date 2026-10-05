---
id: "rtx-tutorial-thread-flags"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication / Thread Flags"
summary: "Keil RTX5 supports up to thirty two thread flags for each thread. These thread flags are stored in the thread control block."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#thread-flags"
license: "Apache-2.0"
mode: "V"
---

_Part of: Inter-thread Communication_

Keil RTX5 supports up to thirty two thread flags for each thread. These thread flags are stored in the thread control block.
It is possible to halt the execution of a thread until a particular thread flag or group of thread flags are set by another
thread in the system.

The osThreadFlagsWait system calls will suspend execution of the thread and place it into the wait_evnt state.
Execution of the thread will not start until at least one the flags set in the osThreadFlagsWait API call have been
set. It is also possible to define a periodic timeout after which the waiting thread will move back to the ready state, so
that it can resume execution when selected by the scheduler. A value of osWaitForever (0xFFFF) defines an infinite
timeout period.

```c
osEvent osThreadFlagsWait (int32_t flags,int32_t options,uint32_t timeout);
```

The thread flag options are as follows:

| Options             | Description |
|---------------------|-------------|
| osFlagsWaitAny | Wait for any flag to be set(default) |
| osFlagsWaitAll | Wait for all flags to be set |
| osFlagsNoClear | Do not clear flags that have been specified to wait for |

If a pattern of flags is specified, the thread will resume execution when any one of the specified flags is set (Logic OR).
If the osFlagsWaitAll option is used, then all the flags in the pattern must be set (Logic AND). Any thread can set a
flag on any other thread and a thread may clear its own flags:

```c
int32_t osThredFlagsSet (osThreadId_t  thread_id, int32_t flags);
int32_t osThreadFlagsClear (int32_t signals);
```

#### Exercise 9 - Thread Flags

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 09 Thread Flags** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
