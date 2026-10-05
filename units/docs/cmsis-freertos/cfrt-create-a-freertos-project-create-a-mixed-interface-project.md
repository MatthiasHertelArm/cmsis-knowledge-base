---
id: "cfrt-create-a-freertos-project-create-a-mixed-interface-project"
type: "concept"
domain: "rtos"
title: "Create a FreeRTOS Project: Create a Mixed-Interface Project"
summary: "Using CMSIS-RTOS2 API and native FreeRTOS API simultaneously is possible and some projects do require using the native FreeRTOS API and the CMSIS-RTOS2 API at the same time. Such project should be created as CMSIS-FreeRTOS project."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/create_project.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/create_project.md#create-a-mixed-interface-project"
license: "Apache-2.0"
mode: "V"
---

Using CMSIS-RTOS2 API and native FreeRTOS API simultaneously is possible and some projects do require
using the native FreeRTOS API and the CMSIS-RTOS2 API at the same time. Such project should be
[created as CMSIS-FreeRTOS project](#create_cmsis_project).

Depending on the application requirements, FreeRTOS kernel can be started either by using FreeRTOS
native API or by using CMSIS-RTOS2 API.

### Start the Kernel Using CMSIS-RTOS2 API

```c
/*
  Application thread: Initialize and start the Application
*/
void app_main (void *argument) {

  while(1) {
    // Application code
    // ...
  }
}

/*
  Main function: Initialize and start the kernel
*/
int main (void) {
  SystemCoreClockUpdate();

  // Initialize CMSIS-RTOS2
  osKernelInitialize();

  // Create application main thread
  osThreadNew(app_main, NULL, NULL);

  // Start the kernel and execute the first thread
  osKernelStart();

  while(1);
}
```

#### Restrictions

After the kernel is started using CMSIS-RTOS2 API, FreeRTOS native API can be used with the following restrictions:

- `vTaskStartScheduler` must not be called

### Start the Kernel Using Native API

```c
/*
  Application main thread: Initialize and start the application
*/
void app_main (void *argument) {

  while(1) {
    // Application code
    // ...
  }
}

/*
  Main function: Initialize and start the kernel
*/
int main (void) {
  SystemCoreClockUpdate();

  // Setup the Event Recorder (optionally)
  EvrFreeRTOSSetup(0);

  // Create application main thread
  xTaskCreate (app_main, "app_main", 64, NULL, tskIDLE_PRIORITY+1, NULL);

  // Start the kernel and execute the first thread
  vTaskStartScheduler();

  while(1);
}
```

#### Restrictions

After the kernel is started using FreeRTOS native API, CMSIS-RTOS2 API can be used without restrictions.
