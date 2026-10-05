---
id: "intr-visualizing-real-time-data-with-st-what-exactly-can-it-visualize"
type: "concept"
domain: "debug"
title: "Visualizing Real-time Data With STMViewer: What exactly can it visualize?"
summary: "STMViewer consists of two modules which serve a slightly different purpose:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-15-stm-viewer-debug.md"
doc_source: "https://interrupt.memfault.com/blog/stm-viewer-debug#what-exactly-can-it-visualize"
license: "CC-BY-SA-4.0"
mode: "V"
---

STMViewer consists of two modules which serve a slightly different purpose:

### Variable Viewer
Variable Viewer is a module that reads variables' values directly from RAM using ST-Link SWD (only SWDIO, SWCLK, and GND connection is needed). It is asynchronous, which means it samples the memory with the period set on the PC. It is entirely non-intrusive and can log many variables at once. Writing is supported as well. There are some trade-offs, though. The first one is that logged variables' addresses must be constant, meaning they must be globals. Moreover, with more aggressive optimization, some variables may get optimized and fail to be logged.

### Trace Viewer
Trace Viewer is a module that reads and parses SWO (Serial Wire Viewer) data using an ST-Link. You need to connect SWDIO, SWCLK, SWO, and GND to use it. This tool operates synchronously, meaning it visualizes data points at the rate they are produced on the target. A data point can be either a special single-byte flag used to create digital plots or any value that fits within up to 4 bytes, as in the case of 'analog' plots. It incurs minimal performance overhead, involving just a single register write per plot point, as the ITM peripheral handles serialization and timestamping. Trace Viewer can be employed for profiling specific parts of the codebase or visualizing signals that are too fast for the asynchronous Variable Viewer. Its main limitations are the maximum allowed SWO pin baud rate of the ST-Link and that the ITM peripheral is supported only on Cortex M3/M4/M7/M33 cores.
