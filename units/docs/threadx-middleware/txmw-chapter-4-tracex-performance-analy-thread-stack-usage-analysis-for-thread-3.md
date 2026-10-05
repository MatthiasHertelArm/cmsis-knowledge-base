---
id: "txmw-chapter-4-tracex-performance-analy-thread-stack-usage-analysis-for-thread-3"
type: "concept"
domain: "trace"
title: "Chapter 4 - TraceX performance analysis: Thread Stack Usage !Analysis for thread 3."
summary: "Selecting the Generate Thread Stack Usage button or View -> Thread Stack Usage presents the stack usage for each thread in the trace file."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter4.md#thread-stack-usage-analysis-for-thread-3"
license: "MIT"
mode: "V"
---

Selecting the ***Generate Thread Stack Usage*** button or ***View -> Thread Stack Usage*** presents the stack usage for each thread in the trace file. This is accomplished by ThreadX including the current thread stack pointer in many of the trace entries in the file. A stack usage of 100% indicates the stack has overflowed and must be corrected in the application. If there is no thread execution within this trace file, the stack usage for that thread is shown at 0%. The thread stack usage in the sample ThreadX demonstration trace is shown in **Figure 22**.

(figure: Screenshot of the TraceX Thread Stack Usage.)

**FIGURE 22**

The example shown in **Figure 22** indicates that most threads in this trace have between 9% and 12% stack usage.
