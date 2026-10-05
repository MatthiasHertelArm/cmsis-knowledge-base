---
id: "view-event-recorder-api-eventrecorderclockupdate"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderClockUpdate"
summary: "Call this function when a clock change of the Event Recorder timer source has occurred. Typically, this happens when a clock source is switched (i.e. from XTAL to low-power clock)."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderClockUpdate (void)
```


Call this function when a clock change of the Event Recorder timer source has occurred. Typically, this happens when a clock
source is switched (i.e. from XTAL to low-power clock).

**Note:**
- When using CMSIS-RTOS2 System Timer as the clock source for Event Recorder, call this function in the
  first thread that is running after **osKernelStart.**
- Updating the clock frequency of the Event Recorder will lead to a recalculation of previously received packets and thus to
  wrong display of earlier data in the µVision debugger.
