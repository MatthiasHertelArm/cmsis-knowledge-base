---
id: "alp-cmsis-rtx-threads-create-app-main"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Create RTOS threads: Create app_main"
summary: "Right click on the Source folder under the FVP target, and Add a new item. Select C file (.c), and create the app_main.c file with the contents below:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/threads.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/threads/#create-app-main"
license: "CC-BY-SA-4.0"
mode: "V"
---

Right click on the `Source` folder under the `FVP` target, and `Add a new item`. Select `C file (.c)`, and create the `app_main.c` file with the contents below:

```C
#include "cmsis_os2.h"

void thread1(void *);
void thread2(void *);
void thread3(void *);

void app_main (void *argument) {
	osThreadNew(thread1, NULL, NULL);	// Create thread1
	osThreadNew(thread2, NULL, NULL);	// Create thread2
	osThreadNew(thread3, NULL, NULL);	// Create thread3
}
```
