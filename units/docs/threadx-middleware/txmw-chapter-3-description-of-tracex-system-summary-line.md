---
id: "txmw-chapter-3-description-of-tracex-system-summary-line"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: System Summary Line"
summary: "TraceX also provides a single summary line (the top context in Figure 10) that includes all events on the same line. This makes it easy to see an overview of a complex system."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#system-summary-line"
license: "MIT"
mode: "V"
---

TraceX also provides a single summary line (the top context in **Figure 10**) that includes all events on the same line. This makes it easy to see an overview of a complex system. The summary bar is especially beneficial in systems that have many threads. Without such a summary line, you would have to follow complex system interactions using the vertical scroll bar to follow the context of execution.

(figure: Screenshot of the System Summary Line in the Sequential View tab.)


**FIGURE 10**

The summary line contains a summary of the context as well as the corresponding event summary underneath. In the example shown in
**Figure 10,** it is easy to see that ***thread 2*** is executing and interrupted. The interrupt results in preemption by ***thread 3***,
***thread 6***, ***thread 4***, and ***thread 7***, after which ***thread 2*** resumes execution.
