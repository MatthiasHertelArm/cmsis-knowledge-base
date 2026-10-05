---
id: "alp-uv-debug-3-event-recorder-determine-relative-timing-valu"
type: "concept"
domain: "debug"
title: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / Determine Relative Timing Values"
summary: "Start debugging with µVision: Debug using Event Recorder: Debug using Event Recorder / Determine Relative Timing Values"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uv_debug/3_event_recorder/#determine-relative-timing-values"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Debug using Event Recorder_

1. Unselect **Enable** in the Event Recorder window to stop the collection of data.
2. Right-click on the first in a sequence of stdout frames and select **Set Time Reference**. The selected frame will turn from blue to green.
4. Position your mouse pointer on the **Time (sec)** column on the next event frame.
5. A box will open displaying the elapsed time. It took about one second from the start of this printf to the next one:  
   (figure: Time reference in the Event Recorder window)
6. Enable the Event Recorder so the frames continue to be captured and displayed.
7. You can use this feature to time many different events in your code.

**Notes:**
- Using event annotations provides a useful time link to your source code.
- Using `printf` with a 9600 baud/8 characters UART requires about 80,000 CPU cycles or about 8 msec. Using Event Recorder, it takes only ~500 CPU cycles. Event Recorder is 10 times faster than a UART running at highest speeds. Using an Event such as `StartB(1)` with 8 bytes is even faster: only ~250 CPU cycles.
