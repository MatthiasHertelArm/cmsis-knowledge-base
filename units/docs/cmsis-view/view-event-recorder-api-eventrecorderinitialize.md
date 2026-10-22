---
id: "view-event-recorder-api-eventrecorderinitialize"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderInitialize"
summary: "Call the function EventRecorderInitialize from the user code to set up the Event Recorder. The function initializes all buffers and configures the timer (if configured)."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderInitialize (uint32_t recording, uint32_t start)
```


Call the function **EventRecorderInitialize** from the user code to set up the Event Recorder.
The function initializes all buffers and configures the timer (if configured).

The parameter **\b** recording takes values from EventRecorder_recdefs.

**Code** **Example**
```
int main (void) {                               // main function
  
  HAL_Init();                                   // initialize hardware abstraction layer
  SystemClock_Config();                         // configure the system clock
  MemoryBus_Config();                           // configure the memory bus system

  EventRecorderInitialize (EventRecordAll, 1);	// initialize and start Event Recorder

  ...
}
```
