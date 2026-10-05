---
id: "rtx-tutorial-joinable-threads"
type: "concept"
domain: "rtos"
title: "tutorial: Joinable Threads"
summary: "A new feature in CMSIS-RTOS2 is the ability to create threads in a 'joinable' state. This allows a thead to be created and executed as a standard thread. In addition, a second thread can join it by calling osThreadJoin."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#joinable-threads"
license: "Apache-2.0"
mode: "V"
---

A new feature in CMSIS-RTOS2 is the ability to create threads in a 'joinable' state. This allows a thead to be created and executed as a standard thread. In addition, a second thread can join it by calling osThreadJoin. This will cause the second thread to deschedule and remain in a waiting state until the thread which has been joined is terminated. This allows a temporary joinable thread to be created, which would acquire a block of memory from the global memory pool, this thread could perform some processing and then terminate, releasing the memory back to the memory pool.

A joinable thread can be created by setting the joinable attribute bit in the thread attributes structure as shown below:

```c
static const osThreadAttr_t ThreadAttr_worker = {
    .attr_bits = osThreadJoinable
};
```

Once the thread has been created, it will execute following the same rules as 'normal' threads. Any other thread can then join it by using the OS call:

```c
osThreadJoin(<joinable_thread_handle>);
```

Once osThreadJoin has been called, the thread will deschedule and enter a waiting state until the joinable thread has terminated.

### Exercise 5 - Joinable Threads

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 05 Join** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
