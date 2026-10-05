---
id: "alp-cmsis-rtx-initialize-understanding-the-code"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Initialize the operating system: Understanding the code"
summary: "The function osKernelStart() should never return."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/initialize.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/initialize/#understanding-the-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

The function [osKernelStart()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__KernelCtrl.html#ga9ae2cc00f0d89d7b6a307bba942b5221) should never return.

If your code gets to the infinite `while()` loop, something has gone wrong - most likely with the platform initialization code.

All threads use a prototype of the form:
```C
void thread(void *);
```
where the argument is passed as the second parameter of the [osThreadNew()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__ThreadMgmt.html#ga48d68b8666d99d28fa646ee1d2182b8f) function. Use `NULL` if no argument to pass.

In the above, `app_main` is used as the main application thread, but this naming is arbitrary. From here, you shall spawn all other threads of the RTOS.
