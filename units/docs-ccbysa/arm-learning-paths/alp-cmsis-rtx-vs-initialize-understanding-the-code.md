---
id: "alp-cmsis-rtx-vs-initialize-understanding-the-code"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Initialize the Operating System: Understanding the Code"
summary: "The function osKernelStart() is designed to never return."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/initialize.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/initialize/#understanding-the-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

The function [osKernelStart()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__KernelCtrl.html#ga9ae2cc00f0d89d7b6a307bba942b5221) is designed to never return.

If your code reaches the infinite `while()` loop, something has gone wrong - most likely with the platform initialization code.

All threads should follow a prototype like this:
```C
void thread(void *);
```
The argument for this function is provided as the second parameter of the [osThreadNew()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__ThreadMgmt.html#ga48d68b8666d99d28fa646ee1d2182b8f) function. Use `NULL` if no argument to pass.

In the example above, `app_main` is used as the main application thread, but this naming is arbitrary. From here, you'll spawn all other threads in the RTOS.

**Note:** Tip: Naming the main application thread is flexible. Choose a name that clearly reflects its function.
