---
id: "txmw-chapter-3-description-of-tracex-zooming-in-and-out"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Zooming In and Out"
summary: "By default, TraceX displays the events at their full size. You may zoom in or zoom out as desired."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#zooming-in-and-out"
license: "MIT"
mode: "V"
---

By default, TraceX displays the events at their full size. You may zoom in or zoom out as desired. Zooming out is useful to see the overall events captured in the trace, while zooming in is useful in conditions where the events overlap because of the resolution of the time stamp source. **Figure 19** shows the ***demo_threadx.trx*** file zoomed out so that 100% of the trace file is shown.

(figure: Screenshot of a sample file zoomed out so that 100% of the trace file is shown.)

**FIGURE 19**

When zoomed out at 100% to show the entire trace within the current display page, it is easy to see all the context execution captured in the trace as well as the general events occurring within those contexts. Notice in **Figure 16** that ***thread 1*** and ***thread 2*** execute most often. The blue coloring for their events also suggests that these threads are making queue service calls (queue events are blue in color).

Restoring to a full icon view is equally easy; Either the zoom-in button may be selected repeatedly or some factor of 100 may be entered.
