---
id: "txmw-chapter-3-description-of-tracex-delta-ticks-between-events"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Delta Ticks Between Events"
summary: "Determining the number of ticks between various events in TraceX is easy—click on the starting event and drag the mouse to the ending event."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#delta-ticks-between-events"
license: "MIT"
mode: "V"
---

Determining the number of ticks between various events in TraceX is easy—click on the starting event and drag the mouse to the ending event. The delta number of ticks between the events shows up in the upper right-hand corner of the display, as shown in **Figure 17**.

(figure: Screenshot of the delta number of ticks between the events.)

**FIGURE 17**

The delta ticks shown in **Figure 17** show that 5032 ticks have elapsed between event 125 and event 154. This could also be calculated manually by looking at the relative time stamps in each event and subtracting, but using the GUI is easy and instantaneous.
