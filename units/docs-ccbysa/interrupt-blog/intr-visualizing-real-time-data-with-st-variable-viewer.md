---
id: "intr-visualizing-real-time-data-with-st-variable-viewer"
type: "concept"
domain: "debug"
title: "Visualizing Real-time Data With STMViewer: Variable Viewer"
summary: "As mentioned earlier, Variable Viewer is an asynchronous module that samples values from predefined RAM addresses on your target. It can be particularly useful when visualizing multiple, relatively slow signals (with a maximum sampling rate of around 1 kHz)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-15-stm-viewer-debug.md"
doc_source: "https://interrupt.memfault.com/blog/stm-viewer-debug#variable-viewer"
license: "CC-BY-SA-4.0"
mode: "V"
---



As mentioned earlier, Variable Viewer is an asynchronous module that samples values from predefined RAM addresses on your target. It can be particularly useful when visualizing multiple, relatively slow signals (with a maximum sampling rate of around 1 kHz). The RAM addresses are read from the project's *.elf file and parsed using GDB. This is the same approach used by STMStudio and CubeMonitor.

For a quick start, please refer to [Variable Viewer](https://github.com/klonyyy/STMViewer#variable-viewer-1).

### PID controller
Let's see Variable Viewer in action on a step response of a classic cascaded PID from a servo drive:



We observe two cascaded controllers: a position PID and a velocity PID. The position PID attempts to follow the target and generates velocity targets for the lower-level controller, which, in turn, generates torque setpoints. When the responses are plotted, it's easy to notice the overshoots in the velocity PID response, which helps fine-tune the gains. Moreover, we can see when the velocity target limit is being triggered. You can easily measure the most critical parameters of the response using the built-in markers or export a CSV for a more comprehensive analysis.
