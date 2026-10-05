---
id: "txmw-chapter-3-description-of-tracex-display-overview"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Display Overview"
summary: "(figure: Screenshot of the main display window of the TraceX system analysis tool.)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#display-overview"
license: "MIT"
mode: "V"
---

**Figure 4** shows the main display window of the TraceX system analysis tool. The layout is straightforward—the execution contexts are represented by the vertical elements on the left side; e.g., initialization, interrupt, idle, and the various thread entries. The events that take place in each context are displayed horizontally on the same context line. For example, the **QR** events shown below show that ***thread 2*** is making successive calls to ***tx_queue_receive***.

(figure: Screenshot of the main display window of the TraceX system analysis tool.)


**FIGURE 5**

Context changes are represented by the vertical black lines that connect the context lines. The currently selected event is represented by a solid red vertical line. In this example, event 494 is selected.
