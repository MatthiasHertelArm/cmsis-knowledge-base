---
id: "txmw-chapter-3-description-of-tracex-thread-status-information"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Thread Status Information"
summary: "When enabled, TraceX displays the status of each thread via a colored line on the thread's context."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#thread-status-information"
license: "MIT"
mode: "V"
---

When enabled, TraceX displays the status of each thread via a colored line on the thread's context. A green line indicates that the thread is in a "ready" state, while a line of any other color indicates the thread is suspended. For suspended threads, the color of the line indicates the type of ThreadX object that the thread is suspended on. For example, in **Figure 13** the green line on the ***System Timer Thread's*** context starting at event 147 shows that the ***System Timer Thread*** is ready. Prior to event 147 and after event 154, the absence of the green line indicates that the ***System Timer Thread*** is ready. Prior to event 147 and after event 154, the absence of the green line indicates that the ***System Timer Thread*** is suspended.

(figure: Screenshot of the status of each thread via a colored line on the thread's context.)

**FIGURE 14**

There are three modes of thread status display, available via the ***Options -> Status Lines*** menu. The ***Ready Only*** option only shows the ready (green) status lines, but does not display any suspension status lines. This is the default option for TraceX. The ***All On*** option enables the display of all status lines (ready and suspension).

Finally, the ***All Off*** option disables the display of all status lines.
