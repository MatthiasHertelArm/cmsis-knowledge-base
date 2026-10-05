---
id: "alp-cmsis-rtx-initialize-create-main"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Initialize the operating system: Create main()"
summary: "Right click on the Source folder under the FVP target, and Add new item."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/initialize.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/initialize/#create-main"
license: "CC-BY-SA-4.0"
mode: "V"
---

Right click on the `Source` folder under the `FVP` target, and `Add new item`.

Select `C file (.c)`, and create the `main.c`file with the contents below:

```C
#include "RTE_Components.h"
#include  CMSIS_device_header
#include "cmsis_os2.h"

void app_main(void *);

int __attribute__((noreturn)) main (void) {
    SystemCoreClockUpdate();                    // initialize clocks etc

	osKernelInitialize();                       // initialize RTOS

	osThreadNew(app_main, NULL, NULL);          // Create application main thread

	if (osKernelGetState() == osKernelReady)    // If all OK...
		osKernelStart();                        // Start thread execution

	while(1);                                   // If you get to here, something has gone wrong!
}
```
**Arm Development Studio:**
Right-click on the project, and select `New` > `Source File` from the pop-up menu.
