---
id: "txmw-chapter-3-description-of-tracex-time-view-mode"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Time View Mode"
summary: "The time view mode is selected by the Time View button. Figure 9 shows the same event trace as Figure 8 except in time view mode."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#time-view-mode"
license: "MIT"
mode: "V"
---

The time view mode is selected by the ***Time View*** button. **Figure 9** shows the same event trace as **Figure 8** except in time view mode. In this mode, events are shown in a time relative manner, with the solid green bar being used to show execution between events. This mode is useful to see where the bulk of processing is taking place in the system, which can help developers tune their system for greater performance and/or responsiveness.

(figure: Screenshot of the Time View tab.)

**FIGURE 9**

Note also the ruler above the event display in **Figure 9**. This ruler shows relative ticks from the beginning of the trace, as derived from the time stamp instrumented in the event trace logging inside of ThreadX. If the time stamps are too close (low frequency timer), the events will run together. Conversely, if the time stamps are too far apart (high frequency timer), then the events will be too far apart. Choosing the right frequency time stamp is an important consideration in making the time relative view meaningful.
