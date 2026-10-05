---
id: "txmw-chapter-3-description-of-tracex-event-information-display"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Event Information Display"
summary: "TraceX provides detailed information on some 600 run-time events, including ThreadX, FileX, NetX Duo, and USBX API calls and internal events. TraceX also supports up to an additional 61,439 unique user-defined events."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#event-information-display"
license: "MIT"
mode: "V"
---

TraceX provides detailed information on some 600 run-time events, including ThreadX, FileX, NetX Duo, and USBX API calls and internal events. TraceX also supports up to an additional 61,439 unique user-defined events.

Regardless of whether sequential or time display mode is selected, a mouse-over on any event in the display area results in detailed event information displayed near the event. The mouse-over of event 143 in the demonstration ***demo_threadx.trx*** trace file is shown in **Figure 15**:

(figure: Screenshot of the mouse-over of event 143 in a sample trace file)

**FIGURE 15**

Each event displayed contains standard information about ***Context*** and both the ***Relative Time*** and ***Time Stamp***. The Context field shows what context the event took place in. There are exactly four contexts: thread, idle, ISR, and initialization. When an event takes place in a thread context, the thread name and its priority at that time is gathered and displayed as shown above. The ***Relative Time*** shows the relative number of timer ticks from the beginning of the trace. The ***Raw Time Stamp*** displays the raw time source of the event. Finally, all event-specific information is displayed. This information is detailed throughout the remainder of this chapter.

Detailed event information is also available by double clicking on any event. Double clicking on event 143 is shown in **Figure 16**:

(figure: Screenshot of the detailed event information when an event is double clicked.)

**FIGURE 16**

Being able to view multiple events at once gives the user a much richer view of what happened. Seeing them side by side is quite useful since many events are interrelated. This is accomplished by double clicking on multiple events.
