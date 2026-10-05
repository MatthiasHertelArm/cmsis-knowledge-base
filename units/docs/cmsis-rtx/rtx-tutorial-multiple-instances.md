---
id: "rtx-tutorial-multiple-instances"
type: "concept"
domain: "rtos"
title: "tutorial: Multiple Instances"
summary: "One of the interesting possibilities of an RTOS is that you can create multiple running instances of the same base thread code."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#multiple-instances"
license: "Apache-2.0"
mode: "V"
---

One of the interesting possibilities of an RTOS is that you can create multiple running instances of the same base thread code. For example, you could write a thread to control a UART and then create two running instances of the same thread code.

Here, each instance of the UART code could manage a different UART. Then we can create two instances of the thread assigned to different thread handles. A parameter is also passed to allow each instance to identify which UART it is responsible for.

```c
#define UART1 (void *) 1UL
#define UART2 (void *) 2UL
 
ThreadID_1_0 = osThreadNew (thread1, UART1, &ThreadAttr_Task1);
ThreadID_1_1 = osThreadNew (thread1, UART0, &ThreadAttr_Task1);
```

### Exercise 4 - Multiple Instances

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 04 Multiple Instances** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
