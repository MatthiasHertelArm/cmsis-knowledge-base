---
id: "alp-cmsis-rtx-eventrecorder-eventrecorder-data"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Using Event Recorder: EventRecorder Data"
summary: "Edit the threads.c file, and include the header file:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder/#eventrecorder-data"
license: "CC-BY-SA-4.0"
mode: "V"
---

Edit the `threads.c` file, and include the header file:
```C
#include "EventRecorder.h"
```

Add a call in each thread to `EventRecord2()` with the thread number as the second parameter.

For example, to output a `2` for `thread2`, use:
```C
void __attribute__((noreturn)) thread2(void *argument){
	for(;;){
		printf("hello from thread2\n");
		osDelay(1000);
		EventRecord2 (1+EventLevelAPI, 2, 0);
	}
}
```
Save all files, and `rebuild` (`F7`) the example.

Click `Debug` (`Ctrl+F5`), then `Run` (`F5`) to start the application.

Observe the events in the Event Recorder viewer.

Use the filter to hide `STDIO` events, which shall remove the printf strings. Ensure `Unspecified Events` > `0x0` is enabled.

The thread number is output as the first `Value`:

(figure: Screenshot of the Event Viewer displaying EventRecorder Data with thread numbers shown in the Value column#center)
