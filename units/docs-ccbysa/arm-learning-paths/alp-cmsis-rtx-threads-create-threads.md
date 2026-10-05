---
id: "alp-cmsis-rtx-threads-create-threads"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Create RTOS threads: Create threads"
summary: "You can now implement the functionality of the threads themselves. Start with a simple example... each thread will say hello, and then pause for a period, forever."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/threads.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/threads/#create-threads"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can now implement the functionality of the threads themselves. Start with a simple example... each thread will say hello, and then pause for a period, forever.

Right click on the `Source` folder under the `FVP` target, and `Add a new item`. Select `C file (.c)`, and create the `threads.c` file with contents below:
```C
#include "cmsis_os2.h"
#include <stdio.h>

void __attribute__((noreturn)) thread1(void *argument){
	for(;;){
		printf("hello from thread 1\n");
		osDelay(1000);
	}
}

void __attribute__((noreturn)) thread2(void *argument){
	for(;;){
		printf("hello from thread 2\n");
		osDelay(1000);
	}
}

void __attribute__((noreturn)) thread3(void *argument){
	for(;;){
		printf("hello from thread 3\n");
		osDelay(1000);
	}
}
```
