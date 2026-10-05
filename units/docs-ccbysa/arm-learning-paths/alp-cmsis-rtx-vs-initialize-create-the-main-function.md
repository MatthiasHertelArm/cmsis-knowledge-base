---
id: "alp-cmsis-rtx-vs-initialize-create-the-main-function"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Initialize the Operating System: Create the main() function"
summary: "Within the Source Files group, a main.c is automatically created. Click on the file to open it in the text editor."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/initialize.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/initialize/#create-the-main-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

Return to the `CMSIS` view.

Within the `Source Files` group, a `main.c` is automatically created. Click on the file to open it in the text editor.

Delete any auto-generated code and replace it with the following:

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
